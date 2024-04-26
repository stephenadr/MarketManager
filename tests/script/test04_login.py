import uuid

from tests.api.login import LoginAPI

#登陆专用
class TestLoginAPI():
    uuid = None
    def setup_method(self):
        self.login_api = LoginAPI()
        response = self.login_api.get_verify_code()
        TestLoginAPI.uuid = response.json().get("uuid")
        print("uuid:", TestLoginAPI.uuid)
    def teardown_method(self):
        pass
    # 登录成功
    def test01_login_success(self):
        # 1. 获取验证码
        # 2. 登录
        # 3. 断言
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        response=self.login_api.login(test_data=login_data)
        print(response.json())
        assert response.json()["code"] == 200

    # 登录失败（用户名为空）
    def test02_login_fail_username_is_null(self):
        # 1. 获取验证码
        # 2. 登录
        # 3. 断言
        login_data = {
            "username": "",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        response=self.login_api.login(test_data=login_data)
        print(response.json())
        assert response.json()["code"] == 500
    # 登录失败（未注册用户）
    def test03_login_fail_username_is_not_register(self):
        # 1. 获取验证码
        # 2. 登录
        # 3. 断言
        login_data = {
            "username": "admasdasd",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        response=self.login_api.login(test_data=login_data)
        print(response.json())
        assert response.json()["code"] == 500
import uuid

from tests.api.login import LoginAPI

#登陆专用
class TestLoginAPI():
    uuid = None
    def setup_method(self):
        self.login_api = LoginAPI()
        response = self.login_api.get_verify_code()
        TestLoginAPI.uuid = response.json().get("uuid")
        print("uuid:", TestLoginAPI.uuid)
    def teardown_method(self):
        pass
    # 登录成功
    def test01_login_success(self):
        # 1. 获取验证码
        # 2. 登录
        # 3. 断言
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        response=self.login_api.login(test_data=login_data)
        print(response.json())
        assert response.json()["code"] == 200

    # 登录失败（用户名为空）
    def test02_login_fail_username_is_null(self):
        # 1. 获取验证码
        # 2. 登录
        # 3. 断言
        login_data = {
            "username": "",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        response=self.login_api.login(test_data=login_data)
        print(response.json())
        assert response.json()["code"] == 500
    # 登录失败（未注册用户）
    def test03_login_fail_username_is_not_register(self):
        # 1. 获取验证码
        # 2. 登录
        # 3. 断言
        login_data = {
            "username": "admasdasd",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLoginAPI.uuid
        }
        response=self.login_api.login(test_data=login_data)
        print(response.json())
        assert response.json()["code"] == 500