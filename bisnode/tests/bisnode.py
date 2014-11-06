import os

from suds.client import Client

from ..constants import COMPANY_STANDARD_REPORT, COMPANY_RATING_REPORT


def get_bisnode_report_from_file(report_type, file_name):
    url = "https://www.bisgateway.com/brg/services/%s?wsdl" % report_type
    client = Client(url)
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, "r") as response_message_file:
        response_message = response_message_file.read()
    report = client.service.service(__inject={'reply': response_message})
    return report


def get_bisnode_test_standard_report():
    return get_bisnode_report_from_file(COMPANY_STANDARD_REPORT,
                                        'data/standard_report.xml')


def get_bisnode_test_rating_report():
    return get_bisnode_report_from_file(COMPANY_RATING_REPORT,
                                        'data/rating_report.xml')
