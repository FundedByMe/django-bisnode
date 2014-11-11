from django.utils.timezone import now

import factory

from ..models import BisnodeCompanyReport


class BisnodeCompanyReportFactory(factory.DjangoModelFactory):
    FACTORY_FOR = BisnodeCompanyReport

    company_name = ''
    rating = ''
    date_of_rating = None
    registration_date = None
    last_updated = now()
    history_and_operation = ''
    management = ''
    finances = ''
    solvency = ''
    number_of_employees = None
    share_capital = None
