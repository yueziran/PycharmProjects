# 导包
import unittest,logging,requests,pymysql

from parameterized import parameterized

from interface.apiTestHrmSystem import app

# 创建测试类，集成unittest.TestCase
from interface.apiTestHrmSystem.api.emp_api import EmployeeApi
from interface.apiTestHrmSystem.utils import assert_commont_utils, DBUtils, read_add_emp_data, read_query_emp_data, \
    read_update_emp_data, read_delete_emp_data


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_api = EmployeeApi()


    def tearDown(self):
        pass


    def test01_login_successs(self):
        response = self.emp_api.login("13800000002", "123456")
        logging.info("员工登录结果：{}".format(response.json()))
        # 取出令牌，并拼接Bearer 开头的字符串
        token = "Bearer " + response.json().get('data')
        logging.info("取出的令牌：{}".format(token))

        # 设置员工模块所需要的请求头
        headers = {"Content-Type": "application/json", "Authorization": token}
        app.HEADERS = headers
        logging.info("员工模块请求头：{}".format(headers))

    @parameterized.expand(read_add_emp_data)
    def test02_add_emp(self, username, mobile, http_code, success, code, message):
        response_add_emp = self.emp_api.add_emp(username, mobile, headers=app.HEADERS)
        logging.info("添加员工结果：{}".format(response_add_emp.json()))
        # 断言结果
        assert_commont_utils(self, response_add_emp, http_code, success, code, message)
        emp_id = response_add_emp.json().get("data").get("id")
        app.EMPID = emp_id
        logging.info("添加的员工id：{}".format(emp_id))

    @parameterized.expand(read_query_emp_data())
    def test03_query_emp(self, http_code, success, code, message):
        response_query = self.emp_api.query_emp(app.EMPID, app.HEADERS)
        logging.info("查询员工结果：{}".format(response_query.json()))
        # 断言结果
        assert_commont_utils(self, response_query, http_code, success, code, message)

    @parameterized.expand(read_update_emp_data)
    def test04_update_emp(self, username, http_code, success, code, message):
        response_update = self.emp_api.update_emp(app.EMPID, username, app.HEADERS)
        logging.info("修改员工结果：{}".format(response_update.json()))


        # DBUtils():实例化
        # db:enter函数返回值
        with DBUtils() as db:
            # 执行语句
            sql = "select username from bs_user where id = " + app.EMPID
            logging.info("修改后查询sql:{}".format(sql))
            db.execute(sql)
            result = db.fetchall()
            logging.info("修改后查询sql结果：{}".format(result))
            # 断言
            self.assertEqual(username, result[0][0])

        # 断言结果
        assert_commont_utils(self, response_update, http_code, success, code,message)

    @parameterized.expand(read_delete_emp_data)
    def test05_delete_emp(self, http_code, success, code, message):
        response_delete = self.emp_api.delete_emp(app.EMPID, app.HEADERS)
        logging.info("删除员工结果：{}".format(response_delete.json()))
        # 断言结果
        assert_commont_utils(self, response_delete, http_code, success, code, message)