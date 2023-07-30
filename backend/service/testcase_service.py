from dao.testcase_dao import TestcaseDAO
from util.log_util import Log

class TestcaseService:

    def __init__(self):
        self.testcase_dao = TestcaseDAO()
        self.log = Log()


    def get_filter_testcase(self,id):
        """
        查询过滤的测试用例
        :param id:
        :return:
        """
        res = self.testcase_dao.get_testcase(id) # 调用DAO层
        if res:
            return res
        else:
            self.log.info("未查询到当前测试用例")
            return False


    def get_all_testcase(self):
        """
        查询所有测试用例
        :return:
        """
        res = self.testcase_dao.get_all_testcase()
        if res:
            return res
        else:
            self.log.info("未查询到所有测试用例")
            return False


    def create_testcase(self,TestcaseDAO):
        """
        创建测试用例
        :param TestcaseDAO:
        :return:
        """
        res = self.testcase_dao.get_testcase(TestcaseDAO.id)
        if res:
            self.log.info("测试用例已存在，无法新增")
            return False
        else:
            return self.testcase_dao.add_testcase(TestcaseDAO)


    def delete_testcase(self,id):
        """
        删除测试用例
        :param id:
        :return:
        """
        res = self.testcase_dao.get_testcase(id)
        if res:
            self.testcase_dao.delete_testcase(id)
            self.log.info(f"删除的用例为:{res}")
            return res
        else:
            self.log.info(f"测试用例不存在，无法删除")
            return False



    def update_testcase(self, TestcaseDAO):
        """
        更新测试用例
        :param TestcaseDAO:
        :return:
        """
        res = self.testcase_dao.get_testcase(TestcaseDAO.id)
        if res:
            return self.testcase_dao.update_testcase(TestcaseDAO)
        else:
            self.log.info("修改的测试用例不存在")
            return False


