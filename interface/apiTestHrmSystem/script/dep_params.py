import unittest,logging

from interface.apiTestHrmSystem import app
from interface.apiTestHrmSystem.api.login_api import LoginApi
from interface.apiTestHrmSystem.utils import assert_commont_utils


class TestDep(unittest.TestCase):
    def setUp(self):
        self.login_api = LoginApi()
    def tearDown(self):
        pass

    def test01_login_success(self):
        response=self.login_api.login("13800000002","123456")
        logging.info("登录结果：{}".format(response.json()))
        token = "Bearer " + response.json().get("data")
        logging.info("令牌:{}".format(token))
        # 设置员工模块所需要的请求头
        headers = {"Content-Type": "application/json", "Authorization": token}
        app.HEADERS = headers
        logging.info("部门模块请求头：{}".format(headers))

    def test02_add_dep(self):
        pass

    def test03_query_dep(self):
        pass

    def test04_update_dep(self):
        pass

    def test05_delete_dep(self):
        pass