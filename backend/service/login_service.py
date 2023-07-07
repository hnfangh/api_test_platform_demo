

from dao.user_dao import UserDAO
from util.log_util import Log

userdao = UserDAO()
log = Log()

class LoginService():



    def login(self,id):
        """
        登陆逻辑
        :param userdao:
        :return:
        """
        res = userdao.get_user(id)
        if res:
            return res
        else:
            log.info("未查询到用户信息")
            return False




    def register(self,userdao):
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