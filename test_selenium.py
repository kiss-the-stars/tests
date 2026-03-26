from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# 初始化Chrome浏览器
driver = webdriver.Chrome()
# 访问百度首页
driver.get("https://www.baidu.com")
# 等待搜索框加载完成并输入关键词
from selenium.webdriver.support import expected_conditions as EC

search_box = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "chat-textarea"))
)
search_box.send_keys("selenium")
# 点击搜索按钮
search_button = driver.find_element(By.ID, "chat-submit-button")
search_button.click()
# 验证页面标题
WebDriverWait(driver, 10).until(
    EC.title_contains("selenium")
)
print("Selenium 搜索验证成功！")
# 关闭浏览器
driver.quit()