# 导包
import unittest,logging,requests,pymysql
from interface.apiTestHrmSystem import app

# 创建测试类，集成unittest.TestCase
from interface.apiTestHrmSystem.api.emp_api import EmployeeApi
from interface.apiTestHrmSystem.utils import assert_commont_utils, DBUtils


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_api = EmployeeApi()


    def tearDown(self):
        pass


    # def test_emp_management(self):
    #
    #     """
    #     员工模块增删改查接口测试
    #     :return:
    #     """
    #     """
    #     初始化日志配置信息
    #     """
    #     app.init_logging()
    #
    #     """
    #     调用登录接口
    #     """
    #     response = self.emp_api.login("13800000002", "123456")
    #     logging.info("员工登录结果：{}".format(response.json()))
    #     # 取出令牌，并拼接Bearer 开头的字符串
    #     token = "Bearer " + response.json().get('data')
    #     logging.info("取出的令牌：{}".format(token))
    #
    #     # 设置员工模块所需要的请求头
    #     headers = {"Content-Type":"application/json","Authorization":token}
    #     logging.info("员工模块请求头：{}".format(headers))
    #
    #     """
    #     调用添加员工接口
    #     """
    #     response_add_emp = self.emp_api.add_emp("toggfdddddf52gm", "13072222999", headers=headers)
    #     logging.info("添加员工结果：{}".format(response_add_emp.json()))
    #     # 断言结果
    #     assert_commont_utils(self, response_add_emp, 200, True, 10000, "操作成功！")
    #
    #     """
    #     调用查询员工接口
    #     """
    #     emp_id = response_add_emp.json().get("data").get("id")
    #     logging.info("添加的员工id：{}".format(emp_id))
    #     response_query = self.emp_api.query_emp(emp_id,headers)
    #     logging.info("查询员工结果：{}".format(response_query.json()))
    #     # 断言结果
    #     assert_commont_utils(self, response_query, 200, True, 10000, "操作成功！")
    #
    #     """
    #     调用修改员工接口
    #     """
    #     response_update = self.emp_api.update_emp(emp_id,"woanin",headers)
    #     logging.info("修改员工结果：{}".format(response_update.json()))
    #     # 断言结果
    #     assert_commont_utils(self, response_update, 200, True, 10000, "操作成功！")
    #
    #     """
    #     调用删除员工接口
    #     """
    #     response_delete = self.emp_api.delete_emp(emp_id,headers)
    #     logging.info("删除员工结果：{}".format(response_delete.json()))
    #     # 断言结果
    #     assert_commont_utils(self, response_delete, 200, True, 10000, "操作成功！")

    """
    加序号，会按顺序执行
    """
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

    def test02_add_emp(self):
        response_add_emp = self.emp_api.add_emp("toggfdddddf52gm", "13072222999", headers=app.HEADERS)
        logging.info("添加员工结果：{}".format(response_add_emp.json()))
        # 断言结果
        assert_commont_utils(self, response_add_emp, 200, True, 10000, "操作成功！")
        emp_id = response_add_emp.json().get("data").get("id")
        app.EMPID = emp_id
        logging.info("添加的员工id：{}".format(emp_id))

    def test03_query_emp(self):
        response_query = self.emp_api.query_emp(app.EMPID, app.HEADERS)
        logging.info("查询员工结果：{}".format(response_query.json()))
        # 断言结果
        assert_commont_utils(self, response_query, 200, True, 10000, "操作成功！")

    def test03_update_emp(self):
        response_update = self.emp_api.update_emp(app.EMPID, "woanin", app.HEADERS)
        logging.info("修改员工结果：{}".format(response_update.json()))


        # 建立连接
        # conn = pymysql.connect(host="182.92.81.159",user= "readuser",password="iHRM_user_2019",database="ihrm")
        # # 获取游标
        # cursor = conn.cursor()
        # # 执行语句
        # sql = "select username from bs_user where id = "+app.EMPID
        # logging.info("修改后查询sql:{}".format(sql))
        # cursor.execute(sql)
        # result = cursor.fetchall()
        # logging.info("修改后查询sql结果：{}".format(result))
        # # 断言
        # self.assertEqual("woanin", result[0][0])
        # # 关闭游标
        # cursor.close()
        # # 关闭连接
        # conn.close()

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
            self.assertEqual("woanin", result[0][0])

        # 断言结果
        assert_commont_utils(self, response_update, 200, True, 10000, "操作成功！")

    def test04_delete_emp(self):
        response_delete = self.emp_api.delete_emp(app.EMPID, app.HEADERS)
        logging.info("删除员工结果：{}".format(response_delete.json()))
        # 断言结果
        assert_commont_utils(self, response_delete, 200, True, 10000, "操作成功！")