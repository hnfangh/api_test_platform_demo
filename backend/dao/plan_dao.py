from do.plan_entity import PlanEntity
from server import db
from util.log_util import Log

log = Log()

class PlanDAO(PlanEntity):


    def get_plan(self, id):
        """
        查询指定计划
        :return:
        """
        plan_dao = PlanDAO.query.filter_by(id=id).first()
        log.info(f"查询单个的计划为：<========{plan_dao}")
        return plan_dao



    def get_all_plan(self):
        """
        查询所有计划
        :return:
        """
        plan_dao = PlanDAO.query.all()
        log.info(f"查询所有的计划为：<========{plan_dao}")
        return plan_dao



    def add_plan(self, PlanEntity):
        """
        创建新增计划
        :param PlanEntity:
        :return: plan_id
        """
        db.session.add(PlanEntity)
        db.session.commit()
        plan_id = PlanEntity.id
        log.info(f"新增的内容为：<========{PlanEntity.id, PlanEntity.name, PlanEntity.testcases}")
        return plan_id
