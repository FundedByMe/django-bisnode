from datetime import date

import factory

from ..models import (
    BisnodeCompanyReport, BisnodeCompanySubReport,
    BisnodeBoardMemberReport, BisnodeFinancialStatementReport)


class BisnodeCompanyReportFactory(factory.DjangoModelFactory):
    FACTORY_FOR = BisnodeCompanyReport

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

    ABSTRACT_FACTORY = True
    FACTORY_FOR = BisnodeCompanySubReport

    created = None


class BisnodeBoardMemberReportFactory(BisnodeCompanySubReportFactory):
    FACTORY_FOR = BisnodeBoardMemberReport

    company_report = factory.SubFactory(BisnodeCompanyReportFactory)
    name = ''
    function = ''
    member_since = None


class BisnodeFinancialStatementReportFactory(BisnodeCompanySubReportFactory):
    FACTORY_FOR = BisnodeFinancialStatementReport

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
