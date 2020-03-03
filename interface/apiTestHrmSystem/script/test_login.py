# 导包
import unittest,logging, requests
# 创建登录测试类，集成unittest.TestCase
from interface.apiTestHrmSystem.api.login_api import LoginApi
from interface.apiTestHrmSystem.utils import assert_commont_utils


class TestLogin(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.login_api = LoginApi()
    def tearDown(self):
        pass

    # 创建登录测试方法

    def test01_login_success(self):
        response = self.login_api.login("13800000002","123456")
        logging.info("登录成功结果：{}".format(response.json()))
        assert_commont_utils(self, response, 200, True, 10000, "操作成功！")

    # 用户名不存在
    def test02_username_not_exist(self):
        response = self.login_api.login("13900000002", "123456")
        logging.info("用户名不存在结果：{}".format(response.json()))
        assert_commont_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码错误
    def test03_password_error(self):
        response = self.login_api.login("13800000002", "error")
        logging.info("密码错误结果：{}".format(response.json()))
        assert_commont_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 无参
    def test04_no_param(self):
        # 按照现有的封装方法，无法对无参进行封装
        response = self.login_api.login_params(None)
        logging.info("无参结果：{}".format(response.json()))
        assert_commont_utils(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！")

    # 用户名为空
    def test05_username_empty(self):
        response = self.login_api.login("", "123456")
        logging.info("用户名为空结果：{}".format(response.json()))
        assert_commont_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码为空
    def test06_password_empty(self):
        response = self.login_api.login("13800000002", "")
        logging.info("密码为空结果：{}".format(response.json()))
        assert_commont_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 少参-缺少mobile
    def test07_param_no_mobile(self):
        jsonData = {"password":"123456"}
        response = self.login_api.login_params(jsonData)
        logging.info("少参-缺少mobile结果：{}".format(response.json()))
        assert_commont_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 少参-缺少password
    def test08_param_no_password(self):
        jsonData = {"mobile": "13800000002"}
        response = self.login_api.login_params(jsonData)
        logging.info("少参-缺少password结果：{}".format(response.json()))
        assert_commont_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 多参-增加一个参数
    def test09_add_param(self):
        jsonData = {"mobile": "13800000002","password": "123456","add_params": "sss"}
        response = self.login_api.login_params(jsonData)
        logging.info("多参-增加一个参数结果：{}".format(response.json()))
        assert_commont_utils(self, response, 200, True, 10000, "操作成功！")

    # 错误参数
    def test10_param_add_one(self):
        jsonData = {"mobile1": "13800000002", "password": "123456"}
        response = self.login_api.login_params(jsonData)
        logging.info("错误参数结果：{}".format(response.json()))
        assert_commont_utils(self, response, 200, False, 20001, "用户名或密码错误")
