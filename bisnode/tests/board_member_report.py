from datetime import date

from django.test import TestCase

from ..models import BisnodeBoardMemberReport
from ..constants import COMPANY_STANDARD_REPORT

from .bisnode import mock_get_bisnode_company_report, TEST_ORGANIZATION_NUMBER
from .factories import (BisnodeCompanyReportFactory,
                        BisnodeBoardMemberReportFactory)


class BisnodeBoardMemberReportTests(TestCase):

    def setUp(self):
        super(BisnodeBoardMemberReportTests, self).setUp()
        self.company_report = BisnodeCompanyReportFactory()
        self.standard_report = mock_get_bisnode_company_report(
            COMPANY_STANDARD_REPORT, TEST_ORGANIZATION_NUMBER)

    def test_create_board_members_reports(self):
        self.assertFalse(self.company_report.board_members.exists())
        BisnodeBoardMemberReport.create_board_members_reports(
            company_report_id=self.company_report.id,
            report=self.standard_report)
        self.assertEqual(self.company_report.board_members.count(), 4)

    def test_create(self):
        self.assertEqual(BisnodeBoardMemberReport.objects.count(), 0)
        board_member = self.standard_report.boardMembers[0]
        board_member_report = BisnodeBoardMemberReportFactory()
        board_member_report.create(self.company_report.id, board_member)
        BisnodeBoardMemberReport.objects.get(
            id=board_member_report.id,
            company_report=self.company_report)
        self.assertEqual(board_member_report.name, 'Skuldman, Per Testperson')
        self.assertEqual(board_member_report.function, '00')
        self.assertEqual(board_member_report.member_since, date(1985, 2, 9))
