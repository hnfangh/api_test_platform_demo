from do.user_entity import UserEntity   # 倒入要执行的实体类包

"""
    数据库表创建,运行文件创建
    注意：创建一次后，就可以注释掉，避免之后每次启动项目都创建
"""

# if __name__ == "__main__":
#     db.create_all()
    # 自动创建用户表 create_all()方法只会创建未被创建的表，而不会删除现有的表。