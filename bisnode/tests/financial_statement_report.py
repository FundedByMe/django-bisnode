from datetime import date

from django.test import TestCase

from money import Money

from ..models import BisnodeFinancialStatementReport

from .factories import BisnodeFinancialStatementReportFactory
from .company_report import BisnodeCompanySubReportTestMixin


class BisnodeFinancialStatementReportTests(BisnodeCompanySubReportTestMixin,
                                           TestCase):

    def test_create_reports(self):
        self.assertFalse(self.company_report.financial_statements.exists())
        BisnodeFinancialStatementReport.create_reports(
            company_report_id=self.company_report.id,
            company_report=self.standard_report)
        self.assertEqual(self.company_report.financial_statements.count(), 5)

    def test_create(self):
        self.assertEqual(BisnodeFinancialStatementReport.objects.count(), 0)
        financial_statement = self.standard_report.financialStatementCommon[0]
        financial_report = BisnodeFinancialStatementReportFactory()
        financial_report.create(self.company_report.id, financial_statement)
        BisnodeFinancialStatementReport.objects.get(
            id=financial_report.id,
            company_report=self.company_report)
        self.assertEqual(financial_report.statement_date, date(2013, 12, 01))
        self.assertEqual(financial_report.number_of_months_covered, 12)
        self.assertEqual(financial_report.total_income,
                         Money(231750000, 'SEK'))
        self.assertEqual(financial_report.income_after_financial_items,
                         Money(11861000, 'SEK'))
        self.assertEqual(financial_report.net_worth, Money(87057000, 'SEK'))
        self.assertEqual(financial_report.total_assets,
                         Money(256405000, 'SEK'))
        self.assertEqual(financial_report.average_number_of_employees, 140)
        self.assertEqual(financial_report.equity_ratio, 34.0)
        self.assertEqual(financial_report.quick_ratio, 105.9)
        self.assertEqual(financial_report.current_ratio, 175.5)
        self.assertEqual(financial_report.profit_margin, 10.2)
        self.assertEqual(financial_report.return_of_total_assets, 9.2)
        self.assertEqual(financial_report.return_on_equity, 13.6)
        self.assertEqual(financial_report.interest_on_liabilities, 3.6)
        self.assertEqual(financial_report.risk_margin, 5.6)
        self.assertEqual(financial_report.liability_ratio, 1.9)
        self.assertEqual(financial_report.interest_cover, 3.8)
        self.assertEqual(financial_report.turnover_assets, 0.9)
