from django.test import TestCase

from mock import patch
from money import Money

from ..models import BisnodeCompanyReport
from ..constants import HIGH, GOOD_FINANCES

from .bisnode import get_bisnode_test_standard_report
from .factories import BisnodeCompanyReportFactory


class BisnodeCompanyReportTests(TestCase):

    def setUp(self):
        super(BisnodeCompanyReportTests, self).setUp()
        self.company_report = BisnodeCompanyReportFactory()
        self.organization_number = "5561234567"
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
    def test_create_rating_report(self, mock_report):
        mock_report.return_value = get_bisnode_test_standard_report()
        self.assert_general_company_data_does_not_exist()
        self.company_report.create_rating_report(self.organization_number)
        self.assert_general_company_data_saved_successfully()

    @patch("bisnode.models.get_bisnode_company_report")
    def test_create_standard_report(self, mock_report):
        mock_report.return_value = get_bisnode_test_standard_report()
        self.assert_general_company_data_does_not_exist()
        self.company_report.create_standard_report(self.organization_number)
        self.assert_general_company_data_saved_successfully()
