from django.test import TestCase

from mock import patch

from ..models import BisnodeRatingReport
from ..constants import GOOD

from .bisnode import MockBisnodeRatingReport
from .factories import BisnodeRatingReportFactory


class BisnodeRatingReportTests(TestCase):

    @patch("bisnode.models.get_bisnode_company_report")
    def test_get_report(self, mock_report):
        mock_report.return_value = MockBisnodeRatingReport(rating=GOOD)
        rating_report = BisnodeRatingReportFactory()
        self.assertIsNone(rating_report.rating)
        self.assertIsNone(rating_report.date_of_rating)
        rating_report.get()
        rating_report = BisnodeRatingReport.objects.get(id=rating_report.id)
        self.assertEquals(rating_report.rating, GOOD)
        self.assertIsNotNone(rating_report.date_of_rating)
        self.assertIsNotNone(rating_report.registration_date)
