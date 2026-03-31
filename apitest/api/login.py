import requests
from ..config import BASE_URL

class LoginAPI:
    def __init__(self):
        # 初始化接口URL（拼接基础域名）
        self.verify_url = f"{BASE_URL}/api/captchaImage"  # 验证码接口
        self.login_url = f"{BASE_URL}/api/login"         # 登录接口

    # 获取验证码
    def get_verify_code(self):
        return requests.get(self.verify_url)

    # 登录（接收外部传入的测试数据）
    def login(self, data):
        headers = {"Content-Type": "application/json"}
        return requests.post(self.login_url, json=data, headers=headers)