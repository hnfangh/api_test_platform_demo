from flask import request
from server import db, app
from util.log_util import Log


class UserDAO(db.Model):
    # 表名
    __tablename__ = "user" # 重新命名，默认按类名来创建表名
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(128),nullable=False)

    def get_user(self, id):
        """
        查询指定用户
        :return:
        """
        with app.app_context():
            return UserDAO.query.filter_by(id=id).all()


    def get_all_user(self):
        """
        查询所有用户
        :return:
        """
        with app.app_context():
            return UserDAO.query.all()


    @app.before_first_request
    def add_user(self,username, password):
        """
        新增用户
        :return:
        """
        with app.app_context():
            user = UserDAO(username=username, password=password)
            Log().info(f"新增的内容为：<========{user}")
            db.session.add(user)
            db.session.commit()

    def update_user(self,id,username,password):
        """
        更新用户
        :param user:
        :return:
        """
        with app.app_context():
            datas = UserDAO.query.filter_by(id=id).first()
            if datas:
                datas.username = username   # 查询的结果datas去替换属性值
                datas.password = password
                Log().info(f"更新的内容为：<========{username,password}")
                db.session.commit()


    def delete_user(self, id):
        """
        删除用户
        :param userid:
        :return:
        """
        with app.app_context():
            datas = UserDAO.query.filter_by(id=id).first()
            if datas:
                Log().info(f"删除的内容为：<========{id}")
                db.session.delete(datas)
                db.session.commit()

if __name__=="__main__":
    user_dao = UserDAO()
    # db.create_all() # 自动创建用户表 create_all()方法只会创建未被创建的表，而不会删除现有的表。
    user_dao.get_all_user()
