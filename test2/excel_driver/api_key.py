import jsonpath
import requests


url="http://39.98.138.157:5000/api/login"

login_data={
    "username":"admin",
    "password":"123456"
}

def  get(self,url,data=None,**kwargs):
    return requests.get(url,data=data,**kwargs)

def post(self,url,data=None,**kwargs):
    return requests.post(url,data=data,**kwargs)