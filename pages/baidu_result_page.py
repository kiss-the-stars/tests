from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaiduResultPage(BasePage):

    def wait_title_contains(self, keyword, timeout=10):
        """
        等待标题包含指定关键词
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.title_contains(keyword),
            f"标题未包含关键词：{keyword}，当前标题：{self.driver.title}"
        )

    def verify_title_contains_keyword(self, keyword):
        """
        验证标题包含关键词
        """
        try:
            self.wait_title_contains(keyword)
            assert f"{keyword}_百度搜索" in self.driver.title, \
                f"标题验证失败！\n期望：{keyword}_百度搜索\n实际：{self.driver.title}"

        except Exception as e:
            raise AssertionError(f"验证异常：{str(e)}")