import os

from suds.client import Client

from ..constants import COMPANY_STANDARD_REPORT, COMPANY_RATING_REPORT

REPORTS_TEST_FILES_DICT = {
    COMPANY_STANDARD_REPORT: 'standard_report.xml',
    COMPANY_RATING_REPORT: 'rating_report.xml',
}

TEST_ORGANIZATION_NUMBER = "5561234567"


def get_test_bisnode_response_message(file_name):
    file_path = os.path.join(os.path.dirname(__file__), 'data', file_name)
    with open(file_path, "r") as message_file:
        response_message = message_file.read()
    return response_message


def mock_get_bisnode_company_report(report_type, organization_number):
    url = "https://www.bisgateway.com/brg/services/%s?wsdl" % report_type
    client = Client(url)
    if organization_number == TEST_ORGANIZATION_NUMBER:
        report_file_name = REPORTS_TEST_FILES_DICT[report_type]
        response_message = get_test_bisnode_response_message(report_file_name)
        message_type = 'reply'
    else:
        response_message = get_test_bisnode_response_message("error.xml")
        message_type = 'fault'
    return client.service.service(__inject={message_type: response_message})
