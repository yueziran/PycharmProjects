import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
parentPath = os.path.split(curPath)[0]
rootPath = os.path.split(parentPath)[0]
sys.path.append(rootPath)
# print(curPath)
# print(parentPath)
# print(rootPath)

import time
from HTMLTestRunner_PY3 import HTMLTestRunner
import unittest

from interface.apiTestHrmSystem.script.emp_params import TestEmployee
from interface.apiTestHrmSystem.script.login_params import TestLogin

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmployee))
# 定义生成测试套件的名称
# report_path = os.path.dirname(os.path.abspath(__file__))+"/report/report{}.html".format(time.strftime("%Y%m%d%H%M%S"))
report_path = os.path.dirname(os.path.abspath(__file__))+"/report/report.html"


# 打开测试报告，写入模式打开，然后利用HTMLTestRunner_PY3插件生成测试报告
with open(report_path, mode="wb") as f:
    # 实例化HTMLTestRunner_PY3
    runner = HTMLTestRunner(f, verbosity=2, title="ihrm登录接口测试",
                            description="这是用HTMLTestRunner_py3生成报告，更美观")
    # 运行测试套件，生成测试报告
    runner.run(suite)