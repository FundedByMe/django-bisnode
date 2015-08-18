from datetime import date

import factory

from ..models import (
    BisnodeCompanyReport, BisnodeCompanySubReport,
    BisnodeBoardMember, BisnodeFinancialStatementCommon,
    BisnodeFinancialStatementSweden, BisnodeHistoricalRating)


class BisnodeCompanyReportFactory(factory.DjangoModelFactory):

    class Meta:
        model = BisnodeCompanyReport

    company_name = ''
    rating = ''
    date_of_rating = None
    registration_date = None
    last_updated = None
    history_and_operation = ''
    management = ''
    finances = ''
    solvency = ''
    number_of_employees = None
    share_capital = None


class BisnodeCompanySubReportFactory(factory.DjangoModelFactory):

    class Meta:
        abstract = True
        model = BisnodeCompanySubReport

    created = None


class BisnodeBoardMemberFactory(BisnodeCompanySubReportFactory):

    class Meta:
        model = BisnodeBoardMember

    company_report = factory.SubFactory(BisnodeCompanyReportFactory)
    name = ''
    function = ''
    member_since = None


class BisnodeFinancialStatementCommonFactory(BisnodeCompanySubReportFactory):

    class Meta:
        model = BisnodeFinancialStatementCommon

    company_report = factory.SubFactory(BisnodeCompanyReportFactory)
    statement_date = date(1800, 12, 01)
    number_of_months_covered = 1
    total_income = None
    income_after_financial_items = None
    net_worth = None
    total_assets = None
    average_number_of_employees = 0
    equity_ratio = 0
    quick_ratio = 0
    current_ratio = 0
    profit_margin = 0
    return_of_total_assets = 0
    return_on_equity = 0
    interest_on_liabilities = 0
    risk_margin = 0
    liability_ratio = 0
    interest_cover = 0
    turnover_assets = 0


class BisnodeFinancialStatementSwedenFactory(BisnodeCompanySubReportFactory):

    class Meta:
        model = BisnodeFinancialStatementSweden

    company_report = factory.SubFactory(BisnodeCompanyReportFactory)
    account_period = date(1800, 12, 01)
    number_of_months_covered = 1
    total_turnover = 0
    total_operating_expenses = 0
    result_after_depreciation = 0
    total_financial_income = 0
    total_financial_costs = 0
    result_after_financial_items = 0
    result_before_allocations = 0
    result_before_tax = 0
    annual_net_profit_loss = 0
    total_intangible_assets = 0
    total_tangible_assets = 0
    total_financial_assets = 0
    total_receivables = 0
    total_current_assets = 0
    total_restricted_equity = 0
    total_non_restricted_capital = 0
    shareholders_equity = 0
    untaxed_reserves = 0
    total_allocations = 0
    total_long_term_liabilities = 0
    total_current_liabilities = 0
    total_equity_and_liability = 0


class BisnodeHistoricalRatingFactory(BisnodeCompanySubReportFactory):

    class Meta:
        model = BisnodeHistoricalRating

    company_report = factory.SubFactory(BisnodeCompanyReportFactory)
    rating = ''
    date_of_rating = None
    date_of_annual_report = None
