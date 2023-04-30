
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# todo 应用配置从py文件读取，便于后期维护
app.config.from_object("util.config.Config")
db = SQLAlchemy(app) # 创建SQLAlchemy对象，并与Flask实例建立关联


@app.route("/")
def hello_flask():
    return "welcome to flask"

if __name__ == "__main__":
    app.run(debug=True)

