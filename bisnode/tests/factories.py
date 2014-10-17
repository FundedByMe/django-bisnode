from django.utils.timezone import now

import factory

from ..models import BisnodeRatingReport


class BisnodeRatingReportFactory(factory.DjangoModelFactory):
    FACTORY_FOR = BisnodeRatingReport

    organization_number = "5561234567"
    rating = None
    date_of_rating = None
    registration_date = None
    last_updated = now()
