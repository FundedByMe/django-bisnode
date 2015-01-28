from datetime import date

from django.test import TestCase

from money import Money

from ..models import BisnodeFinancialStatementSweden
from ..constants import CURRENCY

from .factories import BisnodeFinancialStatementSwedenFactory
from .company_report import BisnodeCompanySubReportTestMixin


class BisnodeFinancialStatementSwedenTests(BisnodeCompanySubReportTestMixin,
                                           TestCase):

    def test_create_reports(self):
        self.assertFalse(
            self.company_report.financial_statements_sweden.exists())
        BisnodeFinancialStatementSweden.create_reports(
            company_report_id=self.company_report.id,
            company_report=self.standard_report)
        self.assertEqual(
            self.company_report.financial_statements_sweden.count(), 5)

    def test_create(self):
        self.assertEqual(
            BisnodeFinancialStatementSweden.objects.count(), 0)
        financial_statement = self.standard_report.financialStatementSweden[0]
        financial_report = BisnodeFinancialStatementSwedenFactory()
        financial_report.create(self.company_report.id, financial_statement)
        BisnodeFinancialStatementSweden.objects.get(
            id=financial_report.id,
            company_report=self.company_report)
        self.assertEqual(financial_report.account_period, date(2013, 12, 01))
        self.assertEqual(financial_report.number_of_months_covered, 12)
        self.assertEqual(financial_report.total_turnover,
                         Money(231750000, CURRENCY))
        self.assertEqual(financial_report.total_operating_expenses,
                         Money(209184000, CURRENCY))
        self.assertEqual(financial_report.result_after_depreciation,
                         Money(22566000, CURRENCY))
        self.assertEqual(financial_report.total_financial_income,
                         Money(1121000, CURRENCY))
        self.assertEqual(financial_report.total_financial_costs,
                         Money(8646000, CURRENCY))
        self.assertEqual(financial_report.result_after_financial_items,
                         Money(11861000, CURRENCY))
        self.assertEqual(financial_report.result_before_allocations,
                         Money(11861000, CURRENCY))
        self.assertEqual(financial_report.result_before_tax,
                         Money(8305000, CURRENCY))
        self.assertEqual(financial_report.annual_net_profit_loss,
                         Money(-2706000, CURRENCY))
        self.assertEqual(financial_report.total_intangible_assets,
                         Money(16800000, CURRENCY))
        self.assertEqual(financial_report.total_tangible_assets,
                         Money(104846000, CURRENCY))
        self.assertEqual(financial_report.total_financial_assets,
                         Money(13383000, CURRENCY))
        self.assertEqual(financial_report.total_receivables,
                         Money(66126000, CURRENCY))
        self.assertEqual(financial_report.total_current_assets,
                         Money(121376000, CURRENCY))
        self.assertEqual(financial_report.total_restricted_equity,
                         Money(20600000, CURRENCY))
        self.assertEqual(financial_report.total_non_restricted_capital,
                         Money(28809000, CURRENCY))
        self.assertEqual(financial_report.shareholders_equity,
                         Money(49409000, CURRENCY))
        self.assertEqual(financial_report.untaxed_reserves,
                         Money(51084000, CURRENCY))
        self.assertEqual(financial_report.total_allocations,
                         Money(0, CURRENCY))
        self.assertEqual(financial_report.total_long_term_liabilities,
                         Money(86766000, CURRENCY))
        self.assertEqual(financial_report.total_current_liabilities,
                         Money(69146000, CURRENCY))
        self.assertEqual(financial_report.total_equity_and_liability,
                         Money(256405000, CURRENCY))
