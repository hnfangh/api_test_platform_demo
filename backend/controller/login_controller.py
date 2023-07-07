from flask import request, jsonify
from flask_restx import Namespace, Resource
from service.login_service import LoginService
from server import api
from util.log_util import Log
from dao.user_dao import UserDAO

loginservice = LoginService()
userdao = UserDAO()
log = Log()

login_ns = Namespace("login", description="登陆")


@login_ns.route("")
class LoginController(Resource):


    post_parser = api.parser()
    post_parser.add_argument("id", type=int, required=True, location="json")
    post_parser.add_argument("username", type=str, required=True, location="json")
    post_parser.add_argument("password", type=str, required=True, location="json")

    @login_ns.expect(post_parser)
    def post(self):
        user_data = request.json
        log.info(f"接收登陆的用户参数<======={user_data}")
        userdao = UserDAO(**user_data)
        # 调用DO层中的as_user_entity_dict(),把python对象转换成前端可以使用的json
        res = loginservice.login(userdao.id).as_user_entity_dict()
        # 把从前端拿到到参数与DB中查询数据比对，相同时候登陆成功
        if res == user_data:
            return jsonify({"code":0, "msg":"user login success", "data":res})
        else: #否则登陆失败
            return jsonify({"code":40001, "msg":"user login fail, user or password error", "data":res})


