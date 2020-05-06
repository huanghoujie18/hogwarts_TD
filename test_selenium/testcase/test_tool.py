# 20200209课间练习
from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestTool():
    def setup(self):
        chromeOptions = Options()  # 使用Options，需要from selenium.webdriver.chrome.options import Options
        #9222是端口号，只要是不被占用的端口号都可以
        chromeOptions.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
        self.driver = webdriver.Chrome(options=chromeOptions)  # 使用webdriver，需要from selenium import webdriver
        # 隐式等待，是全局生效的
        self.driver.implicitly_wait(3)
    def test_tool(self):
        # self.driver.find_element(By.LINK_TEXT,'管理工具').click()
        # sleep(1)
        # self.driver.find_element(By.CSS_SELECTOR,'.manageTools_cnt_item_desc_title').click()
        # self.driver.find_element(By.LINK_TEXT,'图片').click()
        # self.driver.find_element(By.LINK_TEXT,'添加图片').click()
        # self.driver.find_element(By.LINK_TEXT,'上传图片').click()
        pass


