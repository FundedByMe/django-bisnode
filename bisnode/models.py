from datetime import date

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

from money.contrib.django.models.fields import MoneyField

from .constants import (COMPANY_RATING_REPORT, COMPANY_STANDARD_REPORT,
                        RATING_CHOICES, OPERATION_CHOICES, MANAGEMENT_CHOICES,
                        FINANCES_CHOICES, SOLVENCY_CHOICES,
                        BOARD_MEMBERS_FUNCTION_CHOICES)
from .bisnode import get_bisnode_company_report
from .utils import format_bisnode_amount, get_node_value


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
    share_capital = MoneyField(null=True, blank=True, default_currency="SEK",
                               decimal_places=2, max_digits=14)

    def _create_company_report(self, organization_number, report_type):
        report = get_bisnode_company_report(
            report_type=report_type,
            organization_number=organization_number)
        company_data = report.generalCompanyData[0]
        get = lambda x, y: get_node_value(company_data, x, y)
        self.company_name = get('companyName', str)
        self.rating = get('ratingCode', str)
        self.date_of_rating = get('dateOfRating', date)
        self.registration_date = get('dateReg', date)
        self.history_and_operation = get('historyCode', str)
        self.management = get('shareholdersCode', str)
        self.finances = get('financeCode', str)
        self.solvency = get('abilityToPay1', str)
        self.number_of_employees = get('noOfEmployees1', int)
        self.share_capital.amount = get('shareCapital', float)
        self.save()
        return report

    def create_rating_report(self, organization_number):
        self._create_company_report(organization_number, COMPANY_RATING_REPORT)
        return self

    def create_standard_report(self, organization_number):
        standard_report = self._create_company_report(organization_number,
                                                      COMPANY_STANDARD_REPORT)
        BisnodeBoardMemberReport.create_reports(self.id, standard_report)
        BisnodeFinancialStatementCommonReport.create_reports(
            self.id, standard_report)
        return self


class BisnodeCompanySubReport(models.Model):

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        get_latest_by = "created"

    @classmethod
    def _get_bisnode_name(cls):
        raise NotImplementedError()

    @classmethod
    def create_reports(cls, company_report_id, company_report):
        today = timezone.now()
        bisnode_reports = getattr(company_report, cls._get_bisnode_name())
        [cls().create(company_report_id, report) for report in bisnode_reports]
        cls.objects.filter(company_report_id=company_report_id,
                           created__lt=today).delete()

    def create(self, company_report_id, bisnode_report):
        raise NotImplementedError()


class BisnodeBoardMemberReport(BisnodeCompanySubReport):

    company_report = models.ForeignKey(BisnodeCompanyReport,
                                       related_name="board_members")
    name = models.CharField(max_length=60)
    function = models.CharField(max_length=2, blank=True,
                                choices=BOARD_MEMBERS_FUNCTION_CHOICES)
    member_since = models.DateField(blank=True, null=True)

    @classmethod
    def _get_bisnode_name(cls):
        return 'boardMembers'

    def create(self, company_report_id, board_member):
        self.company_report_id = company_report_id
        self.name = board_member.principalName
        self.function = get_node_value(board_member, 'principalFunction', str)
        self.member_since = get_node_value(
            board_member, 'dateOfPrincipalApp', date)
        self.save()


class BisnodeFinancialStatementCommonReport(BisnodeCompanySubReport):

    company_report = models.ForeignKey(BisnodeCompanyReport,
                                       related_name="financial_statements")
    statement_date = models.DateField()
    number_of_months_covered = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)])
    total_income = MoneyField(null=True, blank=True, default_currency="SEK",
                              decimal_places=2, max_digits=14)
    income_after_financial_items = MoneyField(
        null=True, blank=True, default_currency="SEK",
        decimal_places=2, max_digits=14)
    net_worth = MoneyField(null=True, blank=True, default_currency="SEK",
                           decimal_places=2, max_digits=14)
    total_assets = MoneyField(null=True, blank=True, default_currency="SEK",
                              decimal_places=2, max_digits=14)
    average_number_of_employees = models.PositiveIntegerField(
        null=True, blank=True)
    equity_ratio = models.DecimalField(null=True, blank=True, decimal_places=2,
                                       max_digits=6)
    quick_ratio = models.DecimalField(null=True, blank=True, decimal_places=2,
                                      max_digits=6)
    current_ratio = models.DecimalField(null=True, blank=True,
                                        decimal_places=2, max_digits=6)
    profit_margin = models.DecimalField(null=True, blank=True,
                                        decimal_places=2, max_digits=6)
    return_of_total_assets = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=6)
    return_on_equity = models.DecimalField(null=True, blank=True,
                                           decimal_places=2, max_digits=6)
    interest_on_liabilities = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=6)
    risk_margin = models.DecimalField(null=True, blank=True, decimal_places=2,
                                      max_digits=6)
    liability_ratio = models.DecimalField(null=True, blank=True,
                                          decimal_places=2, max_digits=6)
    interest_cover = models.DecimalField(null=True, blank=True,
                                         decimal_places=2, max_digits=6)
    turnover_assets = models.DecimalField(null=True, blank=True,
                                          decimal_places=2, max_digits=6)

    @classmethod
    def _get_bisnode_name(cls):
        return 'financialStatementCommon'

    def create(self, company_report_id, statement):
        get = lambda x, y: get_node_value(statement, x, y)
        self.company_report_id = company_report_id
        self.statement_date = get('statementDate', date)
        self.number_of_months_covered = get('noOfMonthsCovered', int)
        self.total_income = format_bisnode_amount(
            get('totalIncome', float))
        self.income_after_financial_items = format_bisnode_amount(
            get('incomeAfterFinItems', float))
        self.net_worth = format_bisnode_amount(get('netWorth', float))
        self.total_assets = format_bisnode_amount(get('totalAssets', float))
        self.average_number_of_employees = get('noOfEmployeesAverage', int)
        self.equity_ratio = get('equityRatio', float)
        self.quick_ratio = get('quickRatio', float)
        self.current_ratio = get('currentRatio', float)
        self.profit_margin = get('profitMargin', float)
        self.return_of_total_assets = get('returnOnTotalAssets', float)
        self.return_on_equity = get('returnOnEquity', float)
        self.interest_on_liabilities = get('interestOnLiabilities', float)
        self.risk_margin = get('riskmargin', float)
        self.liability_ratio = get('liabilityRatio', float)
        self.interest_cover = get('interestCover', float)
        self.turnover_assets = get('turnoverAssets', float)
        self.save()


class BisnodeHistoricalRatingReport(BisnodeCompanySubReport):

    company_report = models.ForeignKey(BisnodeCompanyReport,
                                       related_name="historical_rating")
    rating = models.CharField(max_length=3, choices=RATING_CHOICES, blank=True)
    date_of_rating = models.DateField(blank=True, null=True)
    date_of_annual_report = models.DateField(blank=True, null=True)

    @classmethod
    def _get_bisnode_name(cls):
        return 'historicalRating'

    def create(self, company_report_id, subreport):
        get = lambda x, y: get_node_value(subreport, x, y)
        self.company_report_id = company_report_id
        self.rating = get('historicalRating', str)
        self.date_of_rating = get('dateOfHistoricalRating', date)
        self.date_of_annual_report = get('dateOfAnnualReport', date)
        self.save()
