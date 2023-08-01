from datetime import datetime

from sqlalchemy import Integer, String, ForeignKey, DateTime

from server import db


class BuildEntity(db.Model):

    # 表名
    __tablename__ = "build"
    # 任务ID
    id = db.Column(Integer, primary_key=True)
    # 报告名称
    report = db.Column(String(64), nullable=False)
    # 计划ID外键关联
    plan_id = db.Column(Integer, ForeignKey("plan.id"))
    # 创建时间,格式化输出
    create_time = db.Column(DateTime, nullable=False, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


    def as_build_entity_dict(self):
        # 解决序列化问题： Object of type datetime is not JSON serializable
        return {"plan_id": self.plan_id, "report": self.report, "create_time": str(self.create_time)}