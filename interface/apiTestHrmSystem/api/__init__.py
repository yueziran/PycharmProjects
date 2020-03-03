# 初始化日志配置的代码，应该放在api.__init__.py中
# 因为，所有的接口测试操作，都会通过script脚本运行
# 而script脚本会调用api封装的接口
# 每次调用api接口时，会先运行api模块下的__init__.py文件
# 从而利于这个机制自动的对日志进行初始化操作
# 初始化后，只要调用api的代码，就能够使用logging打印日志

from interface.apiTestHrmSystem import app
import logging
# 初始化日志配置信息
app.init_logging()
# 测试日志信息
# logging.info("在api测试日志信息")


