from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaiduResultPage(BasePage):

    def wait_title_contains(self, keyword, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.title_contains(keyword))

    # 获取当前页面标题（给用例类使用）
    def get_page_title(self):
        return self.driver.title
