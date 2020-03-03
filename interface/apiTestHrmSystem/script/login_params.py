# 导包
import unittest,logging, requests
# 创建登录测试类，集成unittest.TestCase
from parameterized import parameterized

from interface.apiTestHrmSystem import app
from interface.apiTestHrmSystem.api.login_api import LoginApi
from interface.apiTestHrmSystem.utils import assert_commont_utils, read_login_data, DBUtils



class TestLogin(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.login_api = LoginApi()
    def tearDown(self):
        pass

    # 创建登录测试方法
    @parameterized.expand(read_login_data)
    def test01_login_success(self, mobile,password,http_code,success,code,message):
        print(mobile,password,http_code,success,code,message)
        response = self.login_api.login(mobile,password)
        logging.info("登录成功结果：{}".format(response.json()))
        assert_commont_utils(self, response, http_code, success, code, message)

    # def test01_login_success(self):
    #     response = self.login_api.login("13800000002","123456")
    #     logging.info("登录成功结果：{}".format(response.json()))
    #     assert_commont_utils(self, response, 200, True, 10000, "操作成功！")
