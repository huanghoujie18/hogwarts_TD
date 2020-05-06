import time

from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class TestHogwarts():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.driver.get("https://testerhome.com/")
    self.driver.implicitly_wait(5)

  def teardown_method(self):
    time.sleep(5)
    self.driver.quit()

  def test_topic(self) :
      self.driver.find_element(By.CSS_SELECTOR,'[title="MTSC2020 中国互联网测试开发大会议题征集"]').click()




