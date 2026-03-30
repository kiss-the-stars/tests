from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaiduResultPage(BasePage):

    def wait_title_contains(self, keyword, timeout=10):
