from django.test import TestCase

from mock import patch
from money import Money

from ..models import BisnodeStandardReport
from ..constants import WORTHY, GOOD_FINANCES

from .bisnode import MockBisnodeStandardReport
from .factories import BisnodeStandardReportFactory


class BisnodeStandardReportTests(TestCase):

    @patch("bisnode.models.get_bisnode_company_report")
    def test_get_report(self, mock_report):

        number_of_employees = 10
        share_capital = Money(3000000.00, 'SEK')

        mock_report.return_value = MockBisnodeStandardReport(
            rating=WORTHY,
            finances=GOOD_FINANCES,
            number_of_employees=number_of_employees,
            share_capital=share_capital)
        standard_report = BisnodeStandardReportFactory()

        self.assertNotEqual(standard_report.rating, WORTHY)
        self.assertNotEqual(standard_report.finances, GOOD_FINANCES)
        self.assertNotEqual(standard_report.share_capital, share_capital)
        self.assertIsNone(standard_report.number_of_employees)
        standard_report.get()
        standard_report = BisnodeStandardReport.objects.get(
            id=standard_report.id)
        self.assertEquals(standard_report.rating, WORTHY)
        self.assertEquals(standard_report.finances, GOOD_FINANCES)
        self.assertEquals(standard_report.number_of_employees,
                          number_of_employees)
        self.assertEquals(standard_report.share_capital, share_capital)
