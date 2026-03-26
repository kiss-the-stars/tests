import pytest
from pages.baidu_home_page import BaiduHomePage

class TestBaiduSearch:

    @pytest.fixture(autouse=True)
    def setup(self, driver):

        self.driver = driver
        self.home_page = BaiduHomePage(self.driver)
        self.home_page.open()

    @pytest.mark.parametrize("keyword", [
        "Selenium",
        "Python",
        "AI",
        "pytest"
    ])
    def test_search_keyword(self, keyword):
        """校验结果页标题"""
        result_page = self.home_page.search(keyword)
        result_page.verify_title_contains_keyword(keyword)