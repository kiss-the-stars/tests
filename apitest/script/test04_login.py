# script/test04_login.py
from ..api.login import LoginAPI

class TestLogin:
    def setup_method(self):
        """前置处理：实例化接口对象，获取验证码"""
        # 实际环境请替换成你的 base_url
        self.base_url = "http://your-base-url.com"
        self.login_api = LoginAPI(self.base_url)

        # 1. 获取验证码
        verify_response = self.login_api.get_verify_code()
        # 2. 提取uuid（假设接口返回包含uuid）
        self.uuid = verify_response.json().get("uuid")

    def test_login_success(self):
        """基础测试用例：单一场景"""
        # 1. 构造登录数据
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": self.uuid
        }

        # 2. 调用登录接口
        response = self.login_api.login(login_data)

        # 3. 断言
        assert response.status_code == 200
        assert "成功" in response.text
        assert response.json().get("code") == 200