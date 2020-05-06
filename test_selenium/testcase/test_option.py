from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
class TestOptions:
    def setup(self):
        options = webdriver.ChromeOptions()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)

    def test_click(self):
        self.driver.find_element(By.LINK_TEXT,'企业微信').click()
