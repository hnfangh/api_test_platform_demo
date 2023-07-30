
from flask import request, jsonify
from dao.user_dao import UserDAO
from server import api
from util.log_util import Log
from service.user_service import UserService
from flask_restx import Namespace, Resource


# 命名空间
user_ns = Namespace("user", description="用户管理")
userservice = UserService()
log = Log()



"""
    路由层，获取前端返回的数据，并传给service层处理
    路由层封装接口，使用restful的设计风格
"""
@user_ns.route("")
class UserController(Resource):


    get_parser = api.parser()   # 添加如下参数：参数以及类型和对象
    get_parser.add_argument("id", type=int, location="args")

    # 查询接口
    @user_ns.expect(get_parser) # 添加命名空间预期的参数
    def get(self):
        # 拿请求参数用户ID
        user_id = request.args.get("id")
        log.info(f"接收前端传参 <========{user_id}")
        if user_id:
            # 查询单个用户信息
            # datas查询结果为一个UserDAO对象，进行json格式
            # 调用DO层中的as_user_entity_dict(),把python对象转换成前端可以使用的json
            datas = [userservice.get_filter_user(user_id).as_user_entity_dict()] # 调用Service层
            return jsonify({"code":0, "msg":"search success","data":datas})
        else:
            # 否则查询所有用户信息
            datas = userservice.get_all_user() # 调用Service层
            # 返回的是一个列表对象，需要把它转为json对象，否则前端无法接收
            all_data = [data.as_user_entity_dict() for data in datas]
            return jsonify({"code":0, "msg":"search success","data":all_data})



    put_parser = api.parser()   # 添加如下参数：参数以及类型和对象
    put_parser.add_argument("id",type=int, required=True, location="json")
    put_parser.add_argument("username",type=str, required=True, location="json")
    put_parser.add_argument("password",type=str, required=True, location="json")

    # 更新接口
    @user_ns.expect(put_parser) # 添加命名空间预期的参数
    def put(self):
        user_data = request.json
        log.info(f"接收更新用户的参数<========{user_data}")
        userdao = UserDAO(**user_data)  # 接受的参数返回值进行解包
        res = userservice.update_user(userdao)  # 调用Service层
        if res:
            return jsonify({"code":0, "msg":"update success", "data":res})
        else:
            return jsonify({"code":40001, "msg":"update fail", "data":res})




    post_parser = api.parser()  # 添加如下参数：参数以及类型和对象
    post_parser.add_argument("id", type=int, required=True, location="json")
    post_parser.add_argument("username", type=str, required=True, location="json")
    post_parser.add_argument("password", type=str, required=True, location="json")

    # 新增接口
    @user_ns.expect(post_parser)    # 添加命名空间预期的参数
    def post(self):
        user_data = request.json
        log.info(f"接收更新用户的参数<======={user_data}")
        userdao = UserDAO(**user_data)  # 接受的参数返回值进行解包
        res = userservice.create_user(userdao)    #调用Service层
        if res:
            return jsonify({"code":0, "msg":"create success", "data":res})
        else:
            return jsonify({"code":40001, "msg":"create fail", "data":res})



    del_parser = api.parser()   # 添加如下参数：参数以及类型和对象
    del_parser.add_argument("id", type=int, required=True, location="json")

    # 删除接口
    @user_ns.expect(del_parser) # 添加命名空间预期的参数
    def delete(self):
        user_data = request.json
        res = user_data.get("id")
        log.info(f"接收更新用户的参数<======={res}")
        datas = userservice.delete_user(res)    #调用Service层
        if datas:
            return jsonify({"code": 0, "msg": f"user{res} del success"})
        else:
            return jsonify({"code": 40001, "msg": f"user{res} del fail"})
