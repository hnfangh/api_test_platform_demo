

from dao.user_dao import UserDAO
from util.log_util import Log

userdao = UserDAO()
log = Log()


"""
登陆服务层逻辑
"""
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




