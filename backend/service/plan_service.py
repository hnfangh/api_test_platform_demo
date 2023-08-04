from dao.plan_dao import PlanDAO
from util.log_util import Log


class PlanService():


    def __init__(self):
        self.plan_dao = PlanDAO()
        self.log = Log()



    def get_filter_plan(self, id):
        """
        查询指定测试计划
        :param id:
        :return:
        """
        res = self.plan_dao.get_plan(id)  # 调用DAO层
        if res:
            return res
        else:
            self.log.info("未查询到当前测试计划")
            return False



    def get_all_plan(self):
        """
        查询所有测试计划
        :return:
        """
        res = self.plan_dao.get_all_plan() # 调用DAO层
        if res:
            return res
        else:
            self.log.info("未查询到所有测试计划")
            return False


    def create_plan(self, PlanDAO):
        """
        新增测试计划
        :return:
        """
        res = self.plan_dao.get_testcase(PlanDAO.id)
        if res:
            self.log.info("测试计划已存在，无法新增")
            return False
        else:
            return self.plan_dao.add_testcase(PlanDAO)