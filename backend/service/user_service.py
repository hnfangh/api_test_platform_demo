from dao.user_dao import UserDAO
from util.log_util import Log


"""
User的服务层，处理业务逻辑
"""
class UserService:

    def __init__(self):

        self.user_dao = UserDAO()
        self.log = Log()

    # 修改用户名&密码
    def update_user(self, UserDAO):
        # 查询需要修改的用例ID
        res = self.user_dao.get_user(UserDAO.id)
        if res:
            return self.user_dao.update_user(UserDAO)# 调用DAO层
        else:
            self.log.info("修改的用户不存在")
            return False

    # 新增用户
    def create_user(self, UserDAO):
        res = self.user_dao.get_user(UserDAO.id)
        if res:
            self.log.info("用户已存在，无法新增")
            return False
        else:
            # 用例不存在时候才可以新增
            return self.user_dao.add_user(UserDAO)   #调用DAO层


    # 删除用户
    def delete_user(self, id):
        res = self.user_dao.get_user(id)
        if res:
            self.user_dao.delete_user(id)  # 调用DAO层
            return res
        else:
            self.log.info("用户不存在，无法删除")
            return False

    # 查询所有用户
    def get_all_user(self):
        res = self.user_dao.get_all_user() # 调用DAO层
        if res:
            return res
        else:
            self.log.info("未查询到所有用户")
            return False


    # 按用户名ID查询
    def get_filter_user(self, id):
        res = self.user_dao.get_user(id) # 调用DAO层
        if res:
            return res
        else:
            self.log.info("未查询到当前用户")
            return False



