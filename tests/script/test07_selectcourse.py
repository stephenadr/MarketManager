from tests.api.course import CourseAPI
from tests.api.login import LoginAPI
import pytest

class Testcourse2API:
    token = None
    @classmethod
    def setup_method(self):
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()
        res_verify = self.login_api.get_verify_code()
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": res_verify.json().get("uuid")
        }
        respose=self.login_api.login(login_data)
        Testcourse2API.token=respose.json().get("token")
        print(Testcourse2API.token)
#查询存在的课程
    def test_01select_success(self):
        response = self.course_api.select_course(test_data="?name=测试开发提升课03", token=Testcourse2API.token)
        print(response.json())
        # 断言响应状态码
        assert 200 == response.status_code
        # 断言msg中包含指定的文字
        assert "成功" in response.text
        # 断言json返回数据中code值
        assert 200 == response.json().get("code")
    # 查询失败（用户未登录）
    def test_02select_fail(self):
        response = self.course_api.select_course(test_data="?subject=6", token="xxx")
        print(response.json())
        # 断言响应状态码
        assert 200 == response.status_code
        # 断言msg中包含指定的文字
        assert "认证失败" in response.text
        # 断言json返回数据中code值
        assert 401 == response.json().get("code")

from tests.api.course import CourseAPI
from tests.api.login import LoginAPI
import pytest

class Testcourse2API:
    token = None
    @classmethod
    def setup_method(self):
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()
        res_verify = self.login_api.get_verify_code()
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": res_verify.json().get("uuid")
        }
        respose=self.login_api.login(login_data)
        Testcourse2API.token=respose.json().get("token")
        print(Testcourse2API.token)
#查询存在的课程
    def test_01select_success(self):
        response = self.course_api.select_course(test_data="?name=测试开发提升课03", token=Testcourse2API.token)
        print(response.json())
        # 断言响应状态码
        assert 200 == response.status_code
        # 断言msg中包含指定的文字
        assert "成功" in response.text
        # 断言json返回数据中code值
        assert 200 == response.json().get("code")
    # 查询失败（用户未登录）
    def test_02select_fail(self):
        response = self.course_api.select_course(test_data="?subject=6", token="xxx")
        print(response.json())
        # 断言响应状态码
        assert 200 == response.status_code
        # 断言msg中包含指定的文字
        assert "认证失败" in response.text
        # 断言json返回数据中code值
        assert 401 == response.json().get("code")

