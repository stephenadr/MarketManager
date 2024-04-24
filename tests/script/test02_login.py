# 需求：登录成功

# 导包
import requests
response = requests.get(url="http://kdtx-test.itheima.net/api/captchaImage")
# 发送请求
url = "http://kdtx-test.itheima.net/api/login"


header_data = {
    "Content-Type": "application/json"
}

login_data = {
    "username": "admin",
    "password": "HM_2023_test",
    "code": 2,
    "uuid": response.json()["uuid"]
}
response = requests.post(url=url, headers=header_data, json=login_data)

# 查看响应
print(response.status_code)
print(response.json())

