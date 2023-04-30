from loguru import logger

class Log:

    # 配置日志输出到文件
    logger.add("../logs/run.log", rotation="10 MB", retention="10 days", level="INFO")

    # 写入日志
    def info(self,msg):
        logger.info(msg)


    def waring(self,msg):
        logger.warning(msg)


    def error(self,msg):
        logger.error(msg)

if __name__ == "__main__":
    Log().info("test msg132")