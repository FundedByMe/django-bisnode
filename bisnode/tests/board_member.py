from datetime import date

from django.test import TestCase

from ..models import BisnodeBoardMember

from .factories import BisnodeBoardMemberFactory
from .company_report import BisnodeCompanySubReportTestMixin


class BisnodeBoardMemberTests(BisnodeCompanySubReportTestMixin, TestCase):

    def test_create_reports(self):
        self.assertFalse(self.company_report.board_members.exists())
        BisnodeBoardMember.create_reports(
            company_report_id=self.company_report.id,
            company_report=self.standard_report)
        self.assertEqual(self.company_report.board_members.count(), 4)

    def test_create(self):
        self.assertEqual(BisnodeBoardMember.objects.count(), 0)
        board_member = self.standard_report.boardMembers[0]
        board_member_report = BisnodeBoardMemberFactory()
        board_member_report.create(self.company_report.id, board_member)
        BisnodeBoardMember.objects.get(
            id=board_member_report.id,
            company_report=self.company_report)
        self.assertEqual(board_member_report.name, 'Skuldman, Per Testperson')
        self.assertEqual(board_member_report.function, '00')
        self.assertEqual(board_member_report.member_since, date(1985, 2, 9))
