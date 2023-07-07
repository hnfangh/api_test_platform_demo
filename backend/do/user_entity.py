from sqlalchemy import Integer, String
from server import db


"""
User表的实体类，与DB字段一致
"""
class UserEntity(db.Model):

    # 表名, 需要重新命名，默认按类名来创建表名
    __tablename__ = "user"
    # 唯一主键ID
    id = db.Column(Integer,primary_key=True)
    # 用户名，唯一，不可为空
    username = db.Column(String(64), nullable=False, unique=True)
    # 密码，不为空
    password = db.Column(String(128), nullable=False)

    def as_user_entity_dict(self):
        return {"id": self.id, "username": self.username, "password": self.password}
