
class Config(object):
    user = "xxx"
    pw = "xxx"
    server = "localhost"
    database = "platform"

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{user}:{pw}@{server}/{database}" # 配置数据库URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False # 关闭异常警告提醒
    SQLALCHEMY_ECHO = True  # 是否显示底层执行的SQL语句