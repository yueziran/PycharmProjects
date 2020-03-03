import requests
class DepartmentApi:
    def __init__(self):
        self.dep_url = "http://182.92.81.159/api/company/department"

    def add_dep(self, name, code, headers):
        jsonData = {
            "name": name,
            "code": code,
            "manager": "咸鱼",
            "introduce": "这是个与众不同的咸鱼",
            "pid": ""
        }
        return requests.post(self.dep_url, json=jsonData, headers = headers)

    def query_dep(self, id, headers):
        query_dep_url = self.dep_url+"/"+id
        return  requests.get(query_dep_url, headers)

if __name__ == '__main__':
    da = DepartmentApi()
    jsonData = requests.post("http://182.92.81.159/api/sys/login", json={"mobile": "13800000002", "password": "123456"})
    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + jsonData.json().get("data")}
    da.add_dep("咸鱼2部", "6969", headers)