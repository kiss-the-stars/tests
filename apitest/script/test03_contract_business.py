# script/test03_contract_business.py (简化版)
from ..api.login import LoginAPI
from ..api.course import CourseAPI

class TestCourseBusiness:
    token = None  # 类属性：保存登录后的token，供后续接口使用

    def setup_method(self):
        # 实例化接口对象
        self.login_api = LoginAPI()
        self.course_api = CourseAPI()

    def test_login_and_add_course(self):
        # 1. 登录获取token
        verify_response = self.login_api.get_verify_code()
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": verify_response.json().get("uuid")
        }
        login_response = self.login_api.login(login_data)
        # 保存token到类属性，供后续接口使用
        TestCourseBusiness.token = login_response.json().get("token")

        # 2. 调用新增课程接口（依赖token）
        course_data = {
            "name": "接口测试课程",
            "subject": "6",
            "price": 999,
            "applicablePerson": "2"
        }
        # 新增课程接口需要携带token在请求头
        course_response = self.course_api.add_course(course_data, TestCourseBusiness.token)

        # 断言
        assert course_response.status_code == 200
        assert "成功" in course_response.text