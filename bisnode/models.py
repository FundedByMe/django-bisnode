from datetime import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from money.contrib.django.models.fields import MoneyField

from .constants import (COMPANY_RATING_REPORT, COMPANY_STANDARD_REPORT,
                        RATING_CHOICES, OPERATION_CHOICES, MANAGEMENT_CHOICES,
                        FINANCES_CHOICES, SOLVENCY_CHOICES,
                        BOARD_MEMBERS_FUNCTION_CHOICES)
from .bisnode import get_bisnode_company_report


def bisnode_date_to_date(bisnode_date):
    if len(bisnode_date) == 6:
        bisnode_date += '01'
    formatted_datetime = datetime.strptime(bisnode_date, "%Y%m%d")
    return formatted_datetime.date()


def k_number_to_number(number):
    return number * 1000


class BisnodeCompanyReport(models.Model):

    last_updated = models.DateTimeField(auto_now=True)

    # General Company Data
    company_name = models.CharField(max_length=100, blank=True)
    rating = models.CharField(max_length=3, choices=RATING_CHOICES, blank=True)
    date_of_rating = models.DateField(blank=True, null=True)
    registration_date = models.DateField(blank=True, null=True)
    history_and_operation = models.CharField(
        max_length=6, choices=OPERATION_CHOICES, blank=True)
    management = models.CharField(
        max_length=6, choices=MANAGEMENT_CHOICES, blank=True)
    finances = models.CharField(
        max_length=6, choices=FINANCES_CHOICES, blank=True)
    solvency = models.CharField(
        max_length=6, choices=SOLVENCY_CHOICES, blank=True)
    number_of_employees = models.IntegerField(null=True, blank=True)
    share_capital = MoneyField(
        default=0, default_currency="SEK", decimal_places=2, max_digits=14)

    def create_rating_report(self, organization_number):
        rating_report = get_bisnode_company_report(
            report_type=COMPANY_RATING_REPORT,
            organization_number=organization_number)
        self._update_general_company_data(rating_report)
        self.save()
        return self

    def create_standard_report(self, organization_number):
        standard_report = get_bisnode_company_report(
            report_type=COMPANY_STANDARD_REPORT,
            organization_number=organization_number)
        self._update_general_company_data(standard_report)
        self._update_board_members_data(standard_report)
        self.save()
        return self

    def _update_general_company_data(self, report):
        company_data = report.generalCompanyData[0]
        self.company_name = company_data.companyName
        self.rating = company_data.ratingCode
        self.date_of_rating = bisnode_date_to_date(company_data.dateOfRating)
        self.registration_date = bisnode_date_to_date(company_data.dateReg)
        self.history_and_operation = company_data.historyCode
        self.management = company_data.shareholdersCode
        self.finances = company_data.financeCode
        self.solvency = company_data.abilityToPay1
        self.number_of_employees = company_data.noOfEmployees1
        self.share_capital.amount = float(company_data.shareCapital)

    def _update_board_members_data(self, report):
        today = datetime.now()
        BisnodeBoardMemberReport.create_board_members_reports(self.id, report)
        self.board_members.filter(created__lt=today).delete()


class BisnodeBoardMemberReport(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    company_report = models.ForeignKey(BisnodeCompanyReport,
                                       related_name="board_members")
    name = models.CharField(max_length=60)
    function = models.CharField(max_length=2, blank=True,
                                choices=BOARD_MEMBERS_FUNCTION_CHOICES)
    member_since = models.DateField(blank=True, null=True)

    @classmethod
    def create_board_members_reports(cls, company_report_id, report):
        [cls().create(company_report_id, board_member)
         for board_member in report.boardMembers]

    def create(self, company_report_id, board_member):
        self.company_report_id = company_report_id
        self.name = board_member.principalName
        self.function = board_member.principalFunction
        member_since = getattr(board_member, 'dateOfPrincipalApp', None)
        if member_since:
            self.member_since = bisnode_date_to_date(member_since)
        self.save()


class BisnodeFinancialStatementReport(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    statement_date = models.DateField()
    number_of_months_covered = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)])
    total_income = MoneyField(default=0, default_currency="SEK",
                              decimal_places=2, max_digits=14)
    income_after_financial_items = MoneyField(
        default=0, default_currency="SEK", decimal_places=2, max_digits=14)
    net_worth = MoneyField(default=0, default_currency="SEK",
                           decimal_places=2, max_digits=14)
    total_assets = MoneyField(default=0, default_currency="SEK",
                              decimal_places=2, max_digits=14)
    average_number_of_employees = models.PositiveIntegerField()
    equity_ratio = models.DecimalField(default=0, decimal_places=2,
                                       max_digits=6)
    quick_ratio = models.DecimalField(default=0, decimal_places=2,
                                      max_digits=6)
    current_ratio = models.DecimalField(default=0, decimal_places=2,
                                        max_digits=6)
    profit_margin = models.DecimalField(default=0, decimal_places=2,
                                        max_digits=6)
    return_of_total_assets = models.DecimalField(default=0, decimal_places=2,
                                                 max_digits=6)
    return_on_equity = models.DecimalField(default=0, decimal_places=2,
                                           max_digits=6)
    interest_on_liabilities = models.DecimalField(default=0, decimal_places=2,
                                                  max_digits=6)
    risk_margin = models.DecimalField(default=0, decimal_places=2,
                                      max_digits=6)
    liability_ratio = models.DecimalField(default=0, decimal_places=2,
                                          max_digits=6)
    interest_cover = models.DecimalField(default=0, decimal_places=2,
                                         max_digits=6)
    turnover_assets = models.DecimalField(default=0, decimal_places=2,
                                          max_digits=6)

    @classmethod
    def create_financial_statements(cls, company_report_id, company_report):
        [cls().create(company_report_id, statement)
         for statement in company_report.financialStatementCommon]

    def create(self, company_report_id, statement):
        self.company_report_id = company_report_id
        self.statement_date = bisnode_date_to_date(statement.statementDate)
        self.number_of_months_covered = statement.noOfMonthsCovered
        self.total_income = k_number_to_number(statement.totalIncome.value)
        self.income_after_financial_items = k_number_to_number(
            statement.incomeAfterFinItems.value)
        self.net_worth = k_number_to_number(statement.netWorth.value)
        self.total_assets = k_number_to_number(statement.totalAssets.value)
        self.average_number_of_employees = statement.noOfEmployeesAverage.value
        self.equity_ratio = statement.equityRatio.value
        self.quick_ratio = statement.quickRatio.value
        self.current_ratio = statement.currentRatio.value
        self.profit_margin = statement.profitMargin.value
        self.return_of_total_assets = statement.returnOnTotalAssets.value
        self.return_on_equity = statement.returnOnEquity.value
        self.interest_on_liabilities = statement.interestOnLiabilities.value
        self.risk_margin = statement.riskmargin.value
        self.liability_ratio = statement.liabilityRatio.value
        self.interest_cover = statement.interestCover.value
        self.turnover_assets = statement.turnoverAssets.value
