import config
from tests.api.contract import ContractAPI
from tests.api.course import CourseAPI
from tests.api.login import LoginAPI
import pytest

class TestContractBusiness:
    token = None
    @classmethod
    def setup_method(self):

        self.login_api=LoginAPI()
        self.contract_api=ContractAPI()
        self.course_api=CourseAPI()
        self.header_data = {
            "Content-Type": "application/json"
        }
    def teardown_method(self):
        pass
    #登录
    def test01_login_success(self):
        # 1. 获取验证码
        res_v = self.login_api.get_verify_code()
        print(res_v.json())
        # 打印uuid数据
        print(res_v.json().get("uuid"))
        login_data={
            "username":"admin",
            "password":"HM_2023_test",
            "code":"2",
            "uuid":res_v.json().get("uuid")
        }
        res_l = self.login_api.login(test_data=login_data)  # 以位置参数形式传递
        TestContractBusiness.token=res_l.json().get("token")

    def test02_add_course(self):
        add_data = { "name": "测试开发提升课01111", "subject": "2","price": 899,"applicablePerson": "2",  "info": "测试开发提升0122222"}
        res_add = self.course_api.add_course(test_data=add_data, token=TestContractBusiness.token)
        print(res_add.json())

    # 3、上传合同成功
    def test03_add_contract(self):
        file=open(config.BASE_PATH+"/tests/data/test.pdf", "rb")
        res_upload = self.contract_api.upload_contract(test_data=file, token=TestContractBusiness.token)
        print(res_upload.json())

    # 4、合同新增成功
    def test04_newadd_contract(self):
        add_data = {"name": "测试82128", "phone": "13612345678", "contractNo": "HT20240557", "subject": "6",
                    "courseId": " 99", "channel": "0", "activityId": 727, "fileName": "xxx"}
        res_add = self.contract_api.add_contract(test_data=add_data, token=TestContractBusiness.token)
        print(res_add.json())





import config
from tests.api.contract import ContractAPI
from tests.api.course import CourseAPI
from tests.api.login import LoginAPI
import pytest

class TestContractBusiness:
    token = None
    @classmethod
    def setup_method(self):

        self.login_api=LoginAPI()
        self.contract_api=ContractAPI()
        self.course_api=CourseAPI()
        self.header_data = {
            "Content-Type": "application/json"
        }
    def teardown_method(self):
        pass
    #登录
    def test01_login_success(self):
        # 1. 获取验证码
        res_v = self.login_api.get_verify_code()
        print(res_v.json())
        # 打印uuid数据
        print(res_v.json().get("uuid"))
        login_data={
            "username":"admin",
            "password":"HM_2023_test",
            "code":"2",
            "uuid":res_v.json().get("uuid")
        }
        res_l = self.login_api.login(test_data=login_data)  # 以位置参数形式传递
        TestContractBusiness.token=res_l.json().get("token")

    def test02_add_course(self):
        add_data = { "name": "测试开发提升课01111", "subject": "2","price": 899,"applicablePerson": "2",  "info": "测试开发提升0122222"}
        res_add = self.course_api.add_course(test_data=add_data, token=TestContractBusiness.token)
        print(res_add.json())

    # 3、上传合同成功
    def test03_add_contract(self):
        file=open(config.BASE_PATH+"/tests/data/test.pdf", "rb")
        res_upload = self.contract_api.upload_contract(test_data=file, token=TestContractBusiness.token)
        print(res_upload.json())

    # 4、合同新增成功
    def test04_newadd_contract(self):
        add_data = {"name": "测试82128", "phone": "13612345678", "contractNo": "HT20240557", "subject": "6",
                    "courseId": " 99", "channel": "0", "activityId": 727, "fileName": "xxx"}
        res_add = self.contract_api.add_contract(test_data=add_data, token=TestContractBusiness.token)
        print(res_add.json())





