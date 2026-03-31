import pytest
from baidutest.pages import BaiduHomePage

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
        # 1. 搜索
        result_page = self.home_page.search(keyword)
        # 2. 等待页面加载完成
        result_page.wait_title_contains(keyword)

        assert keyword in result_page.get_page_title(), \
        f"断言失败！预期包含关键词：{keyword}，实际标题：{result_page.get_page_title()}"
        f"断言失败！预期包含关键词：{keyword}，实际标题：{result_page.get_page_title()}"
