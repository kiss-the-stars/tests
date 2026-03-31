# api/course.py
import requests
from ..config import BASE_URL

class CourseAPI:
    def __init__(self):
        # 拼接完整的接口URL
        self.add_url = f"{BASE_URL}/api/clues/course"

    # 新增课程（需要token认证）
    def add_course(self, data, token):
        headers = {
            "Content-Type": "application/json",
            "Authorization": token  # 携带登录后的token
        }
        return requests.post(self.add_url, json=data, headers=headers)