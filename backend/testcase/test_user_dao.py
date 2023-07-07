from dao.user_dao import UserDAO
from do.user_entity import UserEntity

class TestUserDao:

    def setup(self):
        self.userdao = UserDAO()

    def test_add_user(self):
        user_entity = UserEntity(username='zhangsan' ,password=12345)
        self.userdao.add_user(user_entity)

    def test_get_user(self):
        print(self.userdao.get_user(id=1))


    def test_get_all_user(self):
        print(self.userdao.get_all_user())


    def test_update_user(self):

        user_entity = UserEntity(id=1, username='zhaoliu' ,password=98765)
        self.userdao.update_user(user_entity)

    def test_delete_user(self):
        self.userdao.delete_user(id=1)
