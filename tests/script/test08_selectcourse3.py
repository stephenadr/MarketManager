from tests.api.course import CourseAPI
from tests.api.login import LoginAPI
import pytest

class Testcourse3API:
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
        Testcourse3API.token=respose.json().get("token")
        print(Testcourse3API.token)

    #存在的课程
    def test01_delete_success(self):
        response = self.course_api.delete_course(course_id=110, token=Testcourse3API.token)
        print(response.json())
        assert response.status_code == 200
        assert response.json().get("code") == 200
        assert response.json().get("msg") == "操作成功"
#不存在的课程
    def test02_delete_fail_id_not_exist(self):
        response = self.course_api.delete_course(course_id=444866, token=Testcourse3API.token)
        print(response.json())
        assert response.status_code == 200
        assert response.json().get("code") == 500
        assert response.json().get("msg") == "操作失败"

    def test03_delete_fail(self):
          response = self.course_api.delete_course(course_id=110, token="xxx")
          print(response.json())
          assert response.status_code == 200
          assert response.json().get("code") ==401
          assert '认证失败'in response.json().get("msg")

from tests.api.course import CourseAPI
from tests.api.login import LoginAPI
import pytest

class Testcourse3API:
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
        Testcourse3API.token=respose.json().get("token")
        print(Testcourse3API.token)

    #存在的课程
    def test01_delete_success(self):
        response = self.course_api.delete_course(course_id=110, token=Testcourse3API.token)
        print(response.json())
        assert response.status_code == 200
        assert response.json().get("code") == 200
        assert response.json().get("msg") == "操作成功"
#不存在的课程
    def test02_delete_fail_id_not_exist(self):
        response = self.course_api.delete_course(course_id=444866, token=Testcourse3API.token)
        print(response.json())
        assert response.status_code == 200
        assert response.json().get("code") == 500
        assert response.json().get("msg") == "操作失败"

    def test03_delete_fail(self):
          response = self.course_api.delete_course(course_id=110, token="xxx")
          print(response.json())
          assert response.status_code == 200
          assert response.json().get("code") ==401
          assert '认证失败'in response.json().get("msg")

