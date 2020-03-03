# 存放全局变量，公有的配置函数和类
import logging
import os
from logging import handlers

# 获取当前项目路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 定义全局变量
HEADERS = None
EMPID= None

# 定义一个初始化日志配置的函数
def init_logging():

    # 创建日志器
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)
    # 创建处理器，通过处理器控制日志的打印（打印到控制台和日志文件中）
    # 创建控制台处理器
    sh = logging.StreamHandler()
    # 创建文件处理器
    # 文件处理器作用是把日志写到日志文件中，如果不管理日志文件，日志文件会越来越大
    # 这种情况下，我们需要拆分日志，可以按大小和时间拆分，使用logging模块中的拆分日志的工具进行
    # when = "S", interval = 10 表示两次运行间隔时间超过10秒就会拆分日志
    # backupCount:备份的日志文件数量
    fh = logging.handlers.TimedRotatingFileHandler(BASE_DIR + "/log/ihrm.log",
                                                   when="S",
                                                   interval=10,
                                                   backupCount=3,
                                                   encoding="utf-8")
    # 设置日志的格式
    fmt = '%(asctime)s%(levelname)s[%(name)s][%(filename)s(%(funcName)s:%(lineno)d)]-%(message)s'
    # 创建日志器
    formatter = logging.Formatter(fmt=fmt)
    # 将格式器添加到处理器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将处理器添加到日志器
    logger.addHandler(sh)
    logger.addHandler(fh)

if __name__ == '__main__':
    # 初始化日志配置，由于没有返回日志器，配置函数的所有配置都会配置到logging的root节点
    init_logging()
    # 初始化了root节点，就可以直接使用logging模块打印日志
    logging.info("在app.py测试日志")