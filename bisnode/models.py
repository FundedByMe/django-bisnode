from django.db import models

from .constants import COMPANY_RATING_REPORT, RATING_CHOICES

from .bisnode import get_bisnode_company_report


class BisnodeRatingReport(models.Model):
    organization_number = models.CharField(max_length=10)
    rating = models.CharField(max_length=3, choices=RATING_CHOICES,
                              null=True, blank=True)
    date_of_rating = models.DateField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def get(self):
        rating_report = get_bisnode_company_report(
            report_type=COMPANY_RATING_REPORT,
            organization_number=self.organization_number)
        company_data = rating_report.generalCompanyData[0]
        self.rating_code = company_data['ratingCode']
        self.date_of_rating = company_data['dateOfRating']
        self.save()