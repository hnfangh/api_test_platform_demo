from flask import request, jsonify
from util.log_util import Log
from service.user import UserService

class UserController:

    # 获取接口
    def get(self):
        user_id = request.args.get("id")
        Log().info(f"接收前端传参ID <========{user_id}")
        datas = UserService().get_filter_user_list(user_id) # 调用Service层
        return {"code":0, "msg":"success","data":datas}

    # 更新接口
    def put(self):
        user_data = request.json
        Log().info(f"接收更新用户的参数<========{user_data}")
        user_id = user_data.get("id")
        user_name = user_data.get("username")
        _password = user_data.get("password")
        datas = UserService().edit_user(user_id, user_name, _password) # 调用Service层
        if datas:
            return {"code":0, "msg":"success", "data":datas}
        else:
            return {"code":40001, "msg":"fail", "data":datas}


    # 新增接口
    def post(self):
        user_data = request.json
        Log().info(f"接收更新用户的参数<======={user_data}")
        user_name = user_data.get("username")
        _password = user_data.get("password")
        datas = UserService().create_user(user_name, _password)    #调用Service层
        if datas:
            return jsonify({"code":0, "msg":"success", "data":datas})
        else:
            return jsonify({"code":40001, "msg":"fail", "data":datas})

    # 删除接口
    def delete(self):
        user_data = request.args.get("id")
        Log().info(f"接收更新用户的参数<======={user_data}")
        datas = UserService().delete_user(user_data)    #调用Service层
        if datas:
            return jsonify({"code": 0, "msg": "success", "data": datas})
        else:
            return jsonify({"code": 40001, "msg": "fail", "data": datas})
