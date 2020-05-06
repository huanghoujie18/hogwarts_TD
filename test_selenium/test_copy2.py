
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestSeleniumDemo1():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(5)

    def test_seleniumdemo1(self):
        self.driver.find_element(By.CSS_SELECTOR,'[title="MTSC2020 中国互联网测试开发大会议题征集"]').click()
        # 不明白怎么找到这个
        self.driver.find_element(By.CSS_SELECTOR,'.toc-container > .btn').click()
        # 选择父元素为 .toc-item:nth-child(4) 元素的所有 toc-item-link 元素。
        self.driver.find_element(By.CSS_SELECTOR,'.toc-item:nth-child(4) > .toc-item-link').click()

    def teardown_method(self):
        time.sleep(3)
        self.driver.quit()
