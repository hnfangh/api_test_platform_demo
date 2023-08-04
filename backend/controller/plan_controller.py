from flask import request, jsonify
from flask_restx import Namespace

from dao.plan_dao import PlanDAO
from server import api
from util.log_util import Log
from service.plan_service import PlanService

# 命名空间
plan_ns = Namespace("plan", "测试计划")
log = Log()
planservice = PlanService()


@plan_ns.route("")
class PlanController():


    get_paser = api.parser()
    get_paser.add_argument("id", type=int, location="args")

    def get(self):
        """
        查询计划接口
        :return:
        """
        plan_id = request.args.get("id")
        log.info(f"接收前端传参 <========{plan_id}")
        if plan_id:
            # 查询单个用户信息
            # datas查询结果为一个UserDAO对象，进行json格式
            # 调用DO层中的as_plan_entity_dict(),把python对象转换成前端可以使用的json
            datas = [planservice.get_filter_plan(plan_id).as_plan_entity_dict()]  # 调用Service层
            return jsonify({"code": 0, "msg": "search success", "data": datas})
        else:
            # 否则查询所有用户信息
            datas = planservice.get_all_plan()  # 调用Service层
            # 返回的是一个列表对象，需要把它转为json对象，否则前端无法接收
            all_data = [data.as_plan_entity_dict() for data in datas]
            return jsonify({"code": 0, "msg": "search success", "data": all_data})


    post_parser = api.parser() # 添加如下参数：参数以及类型和对象
    post_parser.add_argument("id", type=int, required=True, location="json")
    post_parser.add_argument("name", type=str, required=True, location="json")
    post_parser.add_argument("testcases", type=str, required=True, location="json")
    def post(self):
        """
        新增计划接口
        :return:
        """
        plan_data = request.json
        log.info(f"接收更新用户的参数<======={plan_data}")
        plandao = PlanDAO(**plan_data)  # 接受的参数返回值进行解包
        res = planservice.create_plan(plandao)  # 调用Service层
        if res:
            return jsonify({"code": 0, "msg": "create success", "data": res})
        else:
            return jsonify({"code": 40001, "msg": "create fail", "data": res})




    def put(self):
        pass


    def delete(self):
        pass