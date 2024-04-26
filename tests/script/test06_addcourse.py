from tests.api.course import CourseAPI
from tests.api.login import LoginAPI
import pytest

class TestcourseAPI:
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
        TestcourseAPI.token=respose.json().get("token")
        print(TestcourseAPI.token)


    def teardown_method(self):
        pass

    # 课程添加成功
    def test_01add_success(self):
            add_data = {
                "name": "测试开发提升课022222",
                "subject": "3",
                "price": 8922,
                "applicablePerson": "2"
            }
            response = self.course_api.add_course(test_data=add_data, token=TestcourseAPI.token)
            print(response.json())
            # 断言响应状态码
            assert 200 == response.status_code
            # 断言返回数据中包含指定的文字
            assert "成功" in response.text
            # 断言json返回数据code值
            assert 200 == response.json().get("code")

    # 课程添加失败（未登录）
    def test_02add_fail(self):
        add_data = {
            "name": "测试开发提升课02",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2"
        }
        response = self.course_api.add_course(test_data=add_data, token="xxx")
        print(response.json())
        # 断言响应状态码
        assert 200 == response.status_code
        # 断言返回数据中包含指定的文字
        assert "认证失败" in response.text
        # 断言json返回数据code值
        assert 401 == response.json().get("code")
