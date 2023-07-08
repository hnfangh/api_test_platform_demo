

from dao.user_dao import UserDAO
from util.log_util import Log

userdao = UserDAO()
log = Log()

"""
注册服务层逻辑
"""
class RegisterService():

    def register(self ,userdao):
        """
        注册逻辑
        :param userdao:
        :return:
        """
        res = userdao.get_user(userdao.id)
        if res:
            log.info("用户已存在，无法注册®️")
            return False
        else:
            return userdao.add_user(userdao)