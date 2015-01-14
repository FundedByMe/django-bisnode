from datetime import date

from django.test import TestCase

from ..models import BisnodeHistoricalRatingReport
from ..constants import HIGH

from .factories import BisnodeHistoricalRatingReportFactory
from .company_report import BisnodeCompanySubReportTestMixin


class BisnodeHistoricalRatingReportTests(BisnodeCompanySubReportTestMixin,
                                         TestCase):

    def test_create_reports(self):
        self.assertFalse(self.company_report.historical_rating.exists())
        BisnodeHistoricalRatingReport.create_reports(
            company_report_id=self.company_report.id,
            company_report=self.standard_report)
        self.assertEqual(self.company_report.historical_rating.count(), 34)

    def test_create(self):
        self.assertEqual(BisnodeHistoricalRatingReport.objects.count(), 0)
        historical_rating = self.standard_report.historicalRating[0]
        historical_rating_report = BisnodeHistoricalRatingReportFactory()
        historical_rating_report.create(self.company_report.id,
                                        historical_rating)
        BisnodeHistoricalRatingReport.objects.get(
            id=historical_rating_report.id,
            company_report=self.company_report)
        self.assertEqual(historical_rating_report.rating, HIGH)
        self.assertEqual(historical_rating_report.date_of_rating,
                         date(2014, 2, 1))
        self.assertEqual(historical_rating_report.date_of_annual_report,
                         date(2013, 12, 1))
