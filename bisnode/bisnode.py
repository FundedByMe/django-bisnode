from django.conf import settings

from suds.client import Client


bisnode_soap_headers = {
    'userPassword': settings.BISNODE_USER_PASSWORD,
    'userId': settings.BISNODE_USER_ID,
    'customerCode': settings.BISNODE_CUSTOMER_CODE,
    'customerCodeOwner': settings.BISNODE_CUSTOMER_OWNER,
    'language': settings.BISNODE_DEFAULT_LANGUAGE,
    'fromCountry': settings.BISNODE_DEFAULT_FROM_COUNTRY,
    'toCountry': settings.BISNODE_DEFAULT_TO_COUNTRY}


def get_bisnode_api_client(service_name):
    url = "https://www.bisgateway.com/brg/services/%s?wsdl" % service_name
    client = Client(url)
    client.set_options(soapheaders=bisnode_soap_headers)
    return client


def get_bisnode_company_report(report_type, organization_number):
    client = get_bisnode_api_client(service_name=report_type)
    criteria = client.factory.create("ns1:Criteria")
    criteria.countryRegNumber = organization_number
    report = client.service.service(criteria)
    return report
