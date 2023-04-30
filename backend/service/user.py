from dao.user import UserDAO


class UserService:


    def __init__(self):
        self.user_dao = UserDAO()

    # 注册用户
    def register(self,username,password):
        self.create_user(username,password)  #调用DAO层

    # 新增用户
    def create_user(self,username,password):
        datas = self.user_dao.get_user(username)
        if datas is None:
            self.user_dao.add_user(username,password)   #调用DAO层

    # 删除用户
    def delete_user(self,id):
        datas = self.user_dao.get_user(id)
        if datas:
            self.user_dao.delete_user(id)  # 调用DAO层

    # 查询所有用户
    def get_all_user_list(self):
        return self.user_dao.get_all_user() # 调用DAO层

    # 按用户名查询
    def get_filter_user_list(self,id):
        return self.user_dao.get_user(id) # 调用DAO层


    # 修改用户名&密码
    def edit_user(self,id,username,password):
        get_user = self.user_dao.get_user(id)
        if get_user:
            self.user_dao.update_user(id,username,password) # 调用DAO层
