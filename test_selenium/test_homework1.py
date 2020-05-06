'''
作业1：进入testerhome，访问社团，访问霍格沃兹测试学院，访问最顶部的第一个帖子。
2020-01-31直接重做。
'''
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestHomework1:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://testerhome.com/')
        #增加隐式等待
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        sleep(6)
        self.driver.quit()

    def test_homework1(self):
        self.driver.find_element(By.LINK_TEXT,'社团').click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT,'霍格沃兹测试学院').click()
        wait_element=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.topics .topic:nth-child(1) .infos .title a')))
        # from selenium.webdriver.support.wait import WebDriverWait
        #from selenium.webdriver.support import expected_conditions
        self.driver.refresh()
        wait_element.find_element(By.CSS_SELECTOR,'.topics .topic:nth-child(1) .infos .title a').click()

