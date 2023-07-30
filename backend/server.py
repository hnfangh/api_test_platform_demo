
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
"""
启动类
"""

app = Flask(__name__)
# todo 应用配置从py文件读取，便于后期维护
app.config.from_object("util.config.Config")
db = SQLAlchemy(app) # 创建SQLAlchemy对象，并与Flask实例建立关联
# 应用程序对象对其进行初始化，定义好SwaggerAPI文档的内容和地址
api = Api(app,version="1.0", title="测试平台API接口", description="TestPlatform API", doc="/doc")


@app.route("/")
def hello_flask():
    return "welcome to flask"

# todo 添加路由，把controller的命名空间加到启动类中，否则swagger无法展示API接口
def add_router():
    from controller.user_controller import user_ns
    from controller.login_controller import login_ns
    from controller.register_controller import register_ns
    from controller.testcase_controller import testcase_ns
    api.add_namespace(user_ns,"/user") # 添加api的命名空间，解决swagger不展示内容的问题
    api.add_namespace(login_ns, "/login")
    api.add_namespace(register_ns, "/register")
    api.add_namespace(testcase_ns, "/testcase")


if __name__ == "__main__":
    add_router()
    app.run(debug=True)

