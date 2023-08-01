
"""测试用例与测试计划\中间表\实体类"""
from sqlalchemy import Column, ForeignKey, Integer

from server import db

testcase_plan_rel = db.Table(
                             "testcase_plan_rel",
                             Column("testcase_id", Integer, ForeignKey("testcase.id"), primary_key=True),
                             Column("plan_id", Integer, ForeignKey("plan.id"), primary_key=True)
                             )

