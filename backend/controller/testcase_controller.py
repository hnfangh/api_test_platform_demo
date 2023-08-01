from flask import request, jsonify
from flask_restx import Resource, Namespace

from dao.testcase_dao import TestcaseDAO
from util.log_util import Log
from server import api
from service.testcase_service import TestcaseService

log = Log()
testcase_service = TestcaseService()


testcase_ns = Namespace("testcase", description="测试用例管理")


@testcase_ns.route("")
class TestcaseController(Resource):



    get_parser = api.parser()
    get_parser.add_argument("id", type=int, location="args")

    @testcase_ns.expect(get_parser)
    def get(self):
        """
        查询用例单个/多个
        :return:
        """
        case_id = request.args.get("id")
        log.info(f"接受的前端参数为：<========={case_id}")
        # 传参数，查询单个
        if case_id:
            res = testcase_service.get_filter_testcase(case_id)
            # 查询存在的ID用例
            if res:
                datas = [testcase_service.get_filter_testcase(case_id).as_testcase_entity_dict()]
                log.info(f"debug=>>>>>>>>>>>>{datas}")
                return jsonify({"code":0, "msg":"search testcase success","data":datas})
            # 查询不存在的ID用例
            else:
                return jsonify({"code": 0, "msg": "search testcase success", "data": res})
        else:
            # 不传参数查询所有
            datas = testcase_service.get_all_testcase()
            all_datas = [data.as_testcase_entity_dict() for data in datas]
            return jsonify({"code":0, "msg":"search all testcase success","data":all_datas})



    put_parser = api.parser()  # 添加如下参数：参数以及类型和对象
    put_parser.add_argument("id", type=int, required=True, location="json")
    put_parser.add_argument("title", type=str, required=True, location="json")
    put_parser.add_argument("level", type=str, required=True, location="json")
    put_parser.add_argument("step", type=str, required=True, location="json")
    put_parser.add_argument("expect", type=str, required=True, location="json")

    @testcase_ns.expect(put_parser)
    def put(self):
        """
        更新用例
        :return:
        """
        testcase_data = request.json
        log.info(f"接收更新测试用例的参数<========{testcase_data}")
        testcase_dao = TestcaseDAO(**testcase_data)
        res = testcase_service.update_testcase(testcase_dao)
        if res:
            return jsonify({"code":0, "msg":"update testcase success", "data":res})
        else:
            return jsonify({"code":40001, "msg":"update testcase fail", "data":res})



    post_parser = api.parser()  # 添加如下参数：参数以及类型和对象
    post_parser.add_argument("id", type=int, required=True, location="json")
    post_parser.add_argument("title", type=str, required=True, location="json")
    post_parser.add_argument("level", type=str, required=True, location="json")
    post_parser.add_argument("step", type=str, required=True, location="json")
    post_parser.add_argument("expect", type=str, required=True, location="json")

    @testcase_ns.expect(post_parser)
    def post(self):
        """
        新增用例
        :return:
        """

        testcase_data = request.json
        log.info(f"接收新增测试用例的参数<========{testcase_data}")
        testcase_dao = TestcaseDAO(**testcase_data)
        res = testcase_service.create_testcase(testcase_dao)
        if res:
            return jsonify({"code":0, "msg":"create testcase success", "data":res})
        else:
            return jsonify({"code":40001, "msg":"create testcase fail", "data":res})



    delete_parser = api.parser()
    delete_parser.add_argument("id", type=int, required=True, location="json")

    @testcase_ns.expect(delete_parser)
    def delete(self):
        """
        删除用例
        :return:
        """
        case_id = request.json.get("id")
        log.info(f"接收删除测试用例的参数<========{case_id}")
        if case_id:
            testcase_service.delete_testcase(case_id)
            return jsonify({"code":0, "msg":"delete testcase success","data":case_id})
        else:
            return jsonify({"code":40001, "msg":"delete testcase fail","data":case_id})
