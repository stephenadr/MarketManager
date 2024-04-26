import json
import jsonpath
import requests

class Api:
    def get_text(self, data=None, key=None):
        dict_data = json.loads(data)
        value_list = jsonpath.jsonpath(dict_data, key)
        return value_list[0]

    def get(self, url, data=None, **kwargs):
        return requests.get(url, data=data, **kwargs)

    def post(self, url, data=None, **kwargs):
        return requests.post(url, data=data, **kwargs)

if __name__ == '__main__':
    api = Api()
    url = "http://39.98.138.157:5000/api/login"

    login_data = {
        "username": "admin",
        "password": "123456"
    }
    res = api.post(url, data=login_data)
    print(res.text)
