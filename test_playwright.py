from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, channel="chrome")
    page = browser.new_page()
    page.goto("https://www.baidu.com")
    page.fill("#chat-textarea", "playwright")
    page.click("#chat-submit-button")
    #等待标题包含指定内容
    expect(page).to_have_title("playwright_百度搜索")

    print("Playwright 搜索验证成功！")
    browser.close()