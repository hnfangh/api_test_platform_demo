from sqlalchemy.orm import relationship

from do.testcase_plan_rel import testcase_plan_rel
from server import db


class PlanEntity(db.Model):
    """
    测试计划实体类
    """
    # 表名
    __tablename__ = "plan"
    # 计划ID主键，唯一标识
    id = db.Column(db.Integer, primary_key=True)
    # 计划名称，不为空，限制64字符且唯一
    name = db.Column(db.String(64), nullable=True, unique=True)

    # 新增外键关联,secondary用来指明中间的关系表，构建额外多对多关系的表
    testcases = relationship("TestcaseEntity", secondary=testcase_plan_rel)

    # 遍历拿到测试用例名称，并且将名称转为字符串格式
    def as_plan_entity_dict(self):
        return {"id": self.id, "name": self.name, "testcase_info": "".join([testcase.title for testcase in self.testcases])}