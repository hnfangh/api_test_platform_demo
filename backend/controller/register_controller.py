
from flask import request, jsonify
from flask_restx import Namespace, Resource
from service.register_service import RegisterService
from server import api
from util.log_util import Log
from dao.user_dao import UserDAO

registerservice = RegisterService()
userdao = UserDAO()
log = Log()

register_ns = Namespace("register", description="注册")


@register_ns.route("")
class RegisterController(Resource):


    post_parser = api.parser()
    post_parser.add_argument("id", type=int, required=True, location="json")
    post_parser.add_argument("username", type=str, required=True, location="json")
    post_parser.add_argument("password", type=str, required=True, location="json")

    @register_ns.expect(post_parser)
    def post(self):
        user_data = request.json
        log.info(f"接收登陆的用户参数<======={user_data}")
        userdao = UserDAO(**user_data)
        res = registerservice.register(userdao)
        # 注册返回有值时，注册成功
        if res:
            return jsonify({"code":0, "msg":"user register success", "data":res})
        else: #否则注册失败
            return jsonify({"code":40001, "msg":"user register fail, userID or username exists", "data":res})


