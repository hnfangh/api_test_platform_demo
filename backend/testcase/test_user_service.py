from service.register_service import RegisterService
from service.user_service import UserService
from dao.user_dao import UserDAO


class TestUserService:

    def setup(self):
        self.user_service = UserService()
        self.user_register = RegisterService()

    def test_register(self):
        userdao = UserDAO(id=2, username="wangda", password=534675675345)
        self.user_register.register(userdao)

    def test_update_user(self):
        userdao = UserDAO(id=1, username="zhangsan", password=1234)
        self.user_service.update_user(userdao)

    def test_create_user(self):
        userdao = UserDAO(id=3, username="laoliu", password=26590)
        self.user_service.create_user(userdao)

    def test_delete_user(self):
        self.user_service.delete_user(id=3)

    def test_get_all_user(self):
        self.user_service.get_all_user()

    def test_get_filter_user(self):
        self.user_service.get_filter_user(id=1)
