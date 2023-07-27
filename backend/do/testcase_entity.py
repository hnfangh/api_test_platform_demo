from server import db


class TestcaseEntity(db.Model):

    # 表名字
    __tablename__ = "testcase"
    # 用例ID,主键
    id = db.Column(db.Integer, primary_key=True)
    # 用例标题，唯一
    title = db.Column(db.String(64), nullable=True, unique=True)
    # 用例等级，不为空
    level = db.Column(db.Integer, nullable=True)
    # 用例步骤，可以重复
    step = db.Column(db.String(128), nullable=True)
    # 预期结果
    expect = db.Column(db.String(64), nullable=True)


    def as_testcase_entity_dict(self):
        return {"id": self.id, "title": self.title, "level": self.level, "step": self.step, "expect": self.expect}