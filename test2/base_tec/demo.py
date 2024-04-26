import jsonpath
import requests


url="http://39.98.138.157:5000/api/login"

login_data={
    "username":"admin",
    "password":"123456"
}
r=requests.post(url=url,data=login_data)

#嵌套字典,嵌套的保温
name_value=r.json()["data"]["token"]

#jsonpath库，相对路径  $..token
value=jsonpath.jsonpath(r.json(),"$..token")
#绝对路径
value2=jsonpath.jsonpath(r.json(),"$.data.token")
import jsonpath
import requests


url="http://39.98.138.157:5000/api/login"

login_data={
    "username":"admin",
    "password":"123456"
}
r=requests.post(url=url,data=login_data)

#嵌套字典,嵌套的保温
name_value=r.json()["data"]["token"]

#jsonpath库，相对路径  $..token
value=jsonpath.jsonpath(r.json(),"$..token")
#绝对路径
value2=jsonpath.jsonpath(r.json(),"$.data.token")