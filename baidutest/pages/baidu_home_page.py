from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class BaiduHomePage(BasePage):
    SEARCH_INPUT = (By.ID, "chat-textarea")
    SEARCH_BUTTON = (By.ID, "chat-submit-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.baidu.com"

    def search(self, keyword):
        wait = WebDriverWait(self.driver, timeout=15)
        input_element = wait.until(
            EC.presence_of_element_located(self.SEARCH_INPUT),
            message=f"超时，当前URL: {self.driver.current_url}"
        )

        input_element.send_keys(keyword)

        button = wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        button.click()

        from .baidu_result_page import BaiduResultPage
        return BaiduResultPage(self.driver)