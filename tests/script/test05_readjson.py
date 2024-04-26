#读取json文件
import json

import pytest

import config
from tests.api.login import LoginAPI


def read_login_data(json_file):
    with open(config.BASE_PATH+"/tests/data/login.json", "r", encoding="utf-8") as f:
        test_data = []
        login_data = json.load(f)
        #循环遍历数组
        for item in login_data:
            username = item.get("username")
            password = item.get("password")
            status=item.get("status")
            message=item.get("message")
            code=item.get("code")
            test_data.append((username,password,status,message,code))
    return test_data


class TestLoginAPI:
    uuid = None
    @classmethod
    def setup_method(self):
        # 1. 获取验证码
        # 2. 登录
        # 3. 断言
        self.login_api = LoginAPI()
        # 1. 获取验证码
        response=self.login_api.get_verify_code()
        TestLoginAPI.uuid=response.json().get("uuid")
    def teardown_method(self):
        pass

    @pytest.mark.parametrize("username,password,status,message,code",read_login_data(json_file=config.BASE_PATH+"/tests/data/login.json"))
    def test_login(self,username, password, status, message, code):
        login_data = {
            "username": username,
            "password": password,
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        response=self.login_api.login(test_data=login_data)
        print(response)
        #状态断言
        assert response.status_code==status
        #含有不存在
        assert message in response.text



#读取json文件
import json

import pytest

import config
from tests.api.login import LoginAPI


def read_login_data(json_file):
    with open(config.BASE_PATH+"/tests/data/login.json", "r", encoding="utf-8") as f:
        test_data = []
        login_data = json.load(f)
        #循环遍历数组
        for item in login_data:
            username = item.get("username")
            password = item.get("password")
            status=item.get("status")
            message=item.get("message")
            code=item.get("code")
            test_data.append((username,password,status,message,code))
    return test_data


class TestLoginAPI:
    uuid = None
    @classmethod
    def setup_method(self):
        # 1. 获取验证码
        # 2. 登录
        # 3. 断言
        self.login_api = LoginAPI()
        # 1. 获取验证码
        response=self.login_api.get_verify_code()
        TestLoginAPI.uuid=response.json().get("uuid")
    def teardown_method(self):
        pass

    @pytest.mark.parametrize("username,password,status,message,code",read_login_data(json_file=config.BASE_PATH+"/tests/data/login.json"))
    def test_login(self,username, password, status, message, code):
        login_data = {
            "username": username,
            "password": password,
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        response=self.login_api.login(test_data=login_data)
        print(response)
        #状态断言
        assert response.status_code==status
        #含有不存在
        assert message in response.text



