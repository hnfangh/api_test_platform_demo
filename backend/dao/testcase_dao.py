from server import db
from util.log_util import Log
from do import TestcaseEntity

"""继承testcaseEntity类"""



class TestcaseDAO(TestcaseEntity):
    log = Log()

    def get_testcase(self,id):
        """
        查询测试用例
        :return:
        """
        case_info = TestcaseDAO.query.filter_by(id=id).first()
        self.log.info(f"查询单个测试用例的结果：{case_info}")
        return case_info

    def get_all_testcase(self):
        """
        查询所有测试用例
        :return:
        """
        case_info = TestcaseDAO.query.all()
        self.log.info(f"查询所有测试用例的结果：{case_info}")
        return case_info

    def add_testcase(self,TestcaseEntity):
        """新增测试用例"""
        db.session.add(TestcaseEntity)
        db.session.commit()
        self.log.info(f"新增的测试用例为：{TestcaseEntity}")
        return TestcaseEntity.id


    def delete_testcase(self,id):
        """
        删除测试用例
        :param id:
        :return:
        """
        case_info = TestcaseDAO.query.filter_by(id=id).first()
        self.log.info(f"删除的测试用例为：{id}")
        db.session.delete(case_info)
        db.session.commit()

    def update_testcase(self,TestcaseEntity):
        """
        更新测试用例
        :param TestcaseEntity:
        :return:
        """
        case_info = TestcaseDAO.query.filter_by(id=TestcaseEntity.id).first()
        case_info.title = TestcaseEntity.title
        case_info.step = TestcaseEntity.step
        case_info.level = TestcaseEntity.level
        case_info.expect = TestcaseEntity.expect
        db.session.commit()
        self.log.info(f"更新的测试用例为：{TestcaseEntity}")
        return TestcaseEntity.id