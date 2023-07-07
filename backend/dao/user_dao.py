from server import db, app
from util.log_util import Log
from do.user_entity import UserEntity

"""UserDAO类继承UserEntity实体"""

class UserDAO(UserEntity):




    def get_user(self, id):
        """
        查询指定用户
        :return:
        """
        user_info = UserDAO.query.filter_by(id=id).first()
        Log().info(f"查询单个的内容为：<========{user_info}")
        return user_info



    def get_all_user(self):
        """
        查询所有用户
        :return:
        """
        user_info = UserDAO.query.all()
        Log().info(f"查询多个的内容为：<========{user_info}")
        return user_info



    def add_user(self,UserEntity):
        """
        新增用户
        :return:
        """
        # 把entity的实体类数据添加到session中
        db.session.add(UserEntity)
        db.session.commit()
        user_id = UserEntity.id
        Log().info(f"新增的内容为：<========{UserEntity.id,UserEntity.username,UserEntity.password}")
        return user_id

    def update_user(self,UserEntity):
        """
        更新用户
        :param user:
        :return:
        """
        # 根据ID查询数据
        user_info = self.get_user(UserEntity.id)
        # 将查询的数据属性重新赋值
        user_info.username = UserEntity.username
        user_info.password = UserEntity.password
        db.session.commit() # 重新提交
        # 返回修改用户的ID
        user_id = UserEntity.id
        Log().info(f"修改的内容为: <======{user_id}")
        return user_id



    def delete_user(self, id):
        """
        删除用户
        :param userid:
        :return:
        """

        user_info = UserDAO.query.filter_by(id=id).first()
        Log().info(f"删除的内容为：<========{id}")
        db.session.delete(user_info)
        db.session.commit()
