# 自定义工具类
import os,json

import pymysql

# 封装通用断言函数
def assert_commont_utils(self, response, http_code, success, code, message):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertEqual(message, response.json().get("message"))

# 封装数据库
class DBUtils:
    # 初始化类时，要运行的代码
    def __init__(self, host="182.92.81.159", user="readuser", password="iHRM_user_2019", database="ihrm"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # 代表使用with语法时，进入函数时会先运行enter的代码
    def __enter__(self):
        # 与数据库建立连接
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        # 获取游标
        self.cursor = self.conn.cursor()
        return self.cursor

    # 代表退出with语句块时，会运行exit的代码
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 关闭游标和关闭连接
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

def read_login_data():
    # 定义数据文件路径
    login_data_path = os.path.dirname(os.path.abspath(__file__))+"/data/login.json"
    # 读取数据文件
    with open(login_data_path, mode="r",encoding="utf-8") as f:
        # 使用json模块加载数据为json格式
        jsonData = json.load(f)
        result_list=[]
        # 遍历jsonData
        for case_data in jsonData:
            mobile = case_data.get("mobile")
            password = case_data.get("password")
            http_code = case_data.get("http_code")
            success = case_data.get("success")
            code = case_data.get("code")
            message = case_data.get("message")
            result_list.append((mobile,password,http_code,success,code,message))
        print("读取的数据：{}".format(result_list))
    return result_list




def read_add_emp_data():
    # 定义数据文件路径
    emp_data_path = os.path.dirname(os.path.abspath(__file__))+"/data/emp.json"
    # 读取数据文件
    with open(emp_data_path, mode="r",encoding="utf-8") as f:
        # 使用json模块加载数据为json格式
        # jsonData数据结果：{}
        jsonData = json.load(f)
        result_list=[]

        """
        读取添加员工数据
        """
        add_emp_data = jsonData.get("add_emp")
        username = add_emp_data.get("username")
        mobile = add_emp_data.get("mobile")
        http_code = add_emp_data.get("http_code")
        success = add_emp_data.get("success")
        code = add_emp_data.get("code")
        message = add_emp_data.get("message")
        result_list.append((username, mobile, http_code, success, code, message))

    print("读取添加员工数据：{}".format(result_list))
    return result_list


def read_query_emp_data():
    # 定义数据文件路径
    emp_data_path = os.path.dirname(os.path.abspath(__file__))+"/data/emp.json"
    # 读取数据文件
    with open(emp_data_path, mode="r",encoding="utf-8") as f:
        # 使用json模块加载数据为json格式
        # jsonData数据结果：{}
        jsonData = json.load(f)
        result_list=[]

        # """
        # 读取查询员工数据
        # """
        query_emp_data = jsonData.get("query_emp")
        http_code = query_emp_data.get("http_code")
        success = query_emp_data.get("success")
        code = query_emp_data.get("code")
        message = query_emp_data.get("message")
        result_list.append((http_code, success, code, message))

    print("读取查询员工数据：{}".format(result_list))
    return result_list

def read_update_emp_data():
    # 定义数据文件路径
    emp_data_path = os.path.dirname(os.path.abspath(__file__))+"/data/emp.json"
    # 读取数据文件
    with open(emp_data_path, mode="r",encoding="utf-8") as f:
        # 使用json模块加载数据为json格式
        # jsonData数据结果：{}
        jsonData = json.load(f)
        result_list=[]


        """
        读取修改员工数据
        """
        update_emp_data = jsonData.get("update_emp")
        username = update_emp_data.get("username")
        http_code = update_emp_data.get("http_code")
        success = update_emp_data.get("success")
        code = update_emp_data.get("code")
        message = update_emp_data.get("message")
        result_list.append((username, http_code, success, code, message))

    print("读取修改员工数据：{}".format(result_list))
    return result_list


def read_delete_emp_data():
    # 定义数据文件路径
    emp_data_path = os.path.dirname(os.path.abspath(__file__))+"/data/emp.json"
    # 读取数据文件
    with open(emp_data_path, mode="r",encoding="utf-8") as f:
        # 使用json模块加载数据为json格式
        # jsonData数据结果：{}
        jsonData = json.load(f)
        result_list=[]

        """
        读取删除员工数据
        """
        delete_emp_data = jsonData.get("delete_emp")
        http_code = delete_emp_data.get("http_code")
        success = delete_emp_data.get("success")
        code = delete_emp_data.get("code")
        message = delete_emp_data.get("message")
        result_list.append((http_code, success, code, message))

    print("读取删除员工数据：{}".format(result_list))
    return result_list

# if __name__ == '__main__':
#     read_login_data()