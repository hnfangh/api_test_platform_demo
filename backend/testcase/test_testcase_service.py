from unittest import TestCase

from dao.testcase_dao import TestcaseDAO
from service.testcase_service import TestcaseService


class TestTestcaseService(TestCase):


    def setUp(self) -> None:
        self.testcase_dao = TestcaseDAO()
        self.testcase_service = TestcaseService()



    def test_get_filter_testcase(self):
        self.testcase_service.get_filter_testcase(id=1)


    def test_get_all_testcase(self):
        self.testcase_service.get_all_testcase()

    def test_create_testcase(self):
        testcase_dao  = TestcaseDAO(id=1, title="测试用例001", level="P0" ,step="1.登陆注册，2，新增用例001" ,expect="新增测试用例001成功" )
        self.testcase_service.create_testcase(testcase_dao)


    def test_delete_testcase(self):
        self.testcase_service.delete_testcase(id=1)

    def test_update_testcase(self):
        testcase_dao  = TestcaseDAO(id=1, title="测试用例002", level="P" ,step="002" ,expect="新增测试用例001成功" )
        self.testcase_service.update_testcase(testcase_dao)
