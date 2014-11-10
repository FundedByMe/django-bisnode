from django.test import TestCase

from suds.client import WebFault
from mock import patch
from money import Money

from ..models import BisnodeCompanyReport
from ..constants import (HIGH, GOOD_FINANCES, COMPANY_STANDARD_REPORT,
                         COMPANY_RATING_REPORT)

from .bisnode import mock_get_bisnode_company_report, TEST_ORGANIZATION_NUMBER
from .factories import BisnodeCompanyReportFactory


class BisnodeCompanyReportTests(TestCase):

    def setUp(self):
        super(BisnodeCompanyReportTests, self).setUp()
        self.company_report = BisnodeCompanyReportFactory()
        self.number_of_employees = 6
        self.share_capital = Money(3000000.00, 'SEK')

    def assert_general_company_data_does_not_exist(self):
        self.assertEqual(self.company_report.rating, '')
        self.assertEqual(self.company_report.finances, '')
        self.assertEqual(self.company_report.share_capital, Money(0, 'SEK'))
        self.assertIsNone(self.company_report.number_of_employees)

    def assert_general_company_data_saved_successfully(self):
        self.company_report = BisnodeCompanyReport.objects.get(
            id=self.company_report.id)
        self.assertEquals(self.company_report.rating, HIGH)
        self.assertEquals(self.company_report.finances, GOOD_FINANCES)
        self.assertEquals(self.company_report.number_of_employees,
                          self.number_of_employees)
        self.assertEquals(self.company_report.share_capital, self.share_capital)

    @patch("bisnode.models.get_bisnode_company_report")
    def test_create_rating_report_with_incorrect_input(self, mock_get_report):
        mock_get_report.side_effect = mock_get_bisnode_company_report
        with self.assertRaises(WebFault) as context:
            self.company_report.create_standard_report("000000000")
        self.assertEqual(context.exception.message,
                         "Server raised fault: 'Error in NRG Transaction; "
                         "NRG error code: 532; NRG error message: "
                         "NOT VALID COMPANY'")
        self.assert_general_company_data_does_not_exist()

    @patch("bisnode.models.get_bisnode_company_report")
    def test_create_rating_report(self, mock_get_report):
        mock_get_report.side_effect = mock_get_bisnode_company_report
        self.assert_general_company_data_does_not_exist()
        self.company_report.create_rating_report(TEST_ORGANIZATION_NUMBER)
        mock_get_report.assert_called_with(
            report_type=COMPANY_RATING_REPORT,
            organization_number=TEST_ORGANIZATION_NUMBER)
        self.assert_general_company_data_saved_successfully()

    @patch("bisnode.models.get_bisnode_company_report")
    def test_create_standard_report(self, mock_get_report):
        mock_get_report.side_effect = mock_get_bisnode_company_report
        self.assert_general_company_data_does_not_exist()
        self.company_report.create_standard_report(TEST_ORGANIZATION_NUMBER)
        mock_get_report.assert_called_with(
            report_type=COMPANY_STANDARD_REPORT,
            organization_number=TEST_ORGANIZATION_NUMBER)
        self.assert_general_company_data_saved_successfully()
