# 导包
import requests
# 创建api类
class EmployeeApi:
    def __init__(self):
        pass

    # 封装登录接口
    def login(self, mobile, password):
        self.login_url = "http://182.92.81.159/api/sys/login"
        jsonData = {"mobile": mobile, "password": password}
        return requests.post(self.login_url, json=jsonData)

    # 封装添加员工接口
    def add_emp(self, username, mobile, headers):
        # 调用添加员工
        add_url = "http://182.92.81.159/api/sys/user"
        jsonData = {"username": username,
                    "mobile": mobile,
                    "timeOfEntry": "2019-07-01",
                    "formOfEmployment": 1,
                    "workNumber": "1322131",
                    "departmentName": "开发部",
                    "departmentId": "1066240656856453120",
                    "correctionTime": "2019-11-30"}
        return requests.post(add_url,json=jsonData,headers=headers)

    # 封装查询员工接口
    def query_emp(self, emp_id, headers):
        query_url = "http://182.92.81.159/api/sys/user/" + emp_id
        return requests.get(query_url,headers=headers)

    # 封装修改员工接口
    def update_emp(self, emp_id, username, headers):
        update_url = "http://182.92.81.159/api/sys/user/" + emp_id
        return requests.put(update_url,json={"username": username},headers=headers)

    # 封装删除员工接口
    def delete_emp(self, emp_id, headers):
        delete_url = "http://182.92.81.159/api/sys/user/" + emp_id
        return requests.delete(delete_url,headers=headers)