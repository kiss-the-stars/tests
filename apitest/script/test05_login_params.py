# script/test05_login_params.py
import pytest
from ..api.login import LoginAPI
from ..config import BASE_PATH
import json

# 从JSON文件读取测试数据
# 格式：[("用户名", "密码", 预期状态码, 预期消息, 预期code), ...]
def build_data():
    with open(f"{BASE_PATH}/data/login.json", "r") as f:
        data = json.load(f)
    return [(d["username"], d["password"], d["status"], d["message"], d["code"]) for d in data]

class TestLoginParams:
    def setup_method(self):
        # 前置处理：实例化接口对象，获取验证码
        self.login_api = LoginAPI()
        self.uuid = self.login_api.get_verify_code().json().get("uuid")

    # 参数化装饰器：多组数据批量执行
    @pytest.mark.parametrize("username, password, status, message, code", build_data())
    def test_login(self, username, password, status, message, code):
        login_data = {
            "username": username,
            "password": password,
            "code": "2",
            "uuid": self.uuid
        }
        response = self.login_api.login(login_data)

        # 断言
        assert response.status_code == status
        assert message in response.text
        assert response.json().get("code") == code