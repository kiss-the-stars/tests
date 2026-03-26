class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = None  # 父类默认url，子类会重写

    def open(self):
        """打开页面"""
        if self.url:
            self.driver.get(self.url)
            self.driver.maximize_window()  # 最大化浏览器