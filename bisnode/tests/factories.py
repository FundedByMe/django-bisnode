from django.utils.timezone import now

import factory

from ..models import BisnodeRatingReport, BisnodeStandardReport


class BisnodeReportModelFactory(factory.DjangoModelFactory):
    ABSTRACT_FACTORY = True

    organization_number = "5561234567"
    rating = None
    date_of_rating = None
    registration_date = None
    last_updated = now()


class BisnodeRatingReportFactory(BisnodeReportModelFactory):
    FACTORY_FOR = BisnodeRatingReport


class BisnodeStandardReportFactory(BisnodeReportModelFactory):
    FACTORY_FOR = BisnodeStandardReport

    history_and_operation = ''
    management = ''
    finances = ''
    solvency = ''
    number_of_employees = None
    share_capital = None
