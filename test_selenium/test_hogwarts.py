# Generated by Selenium IDE
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts():
  def setup_method(self):
    # 声明浏览器
    self.driver = webdriver.Chrome()
    self.driver.get("https://testerhome.com/")
    self.driver.maximize_window()
    self.driver.implicitly_wait(5)

  def teardown_method(self):
    time.sleep(5)
    self.driver.quit()

  def test_hogwarts(self) :
    self.driver.find_element(By.LINK_TEXT, "社团").click()
    element=(By.PARTIAL_LINK_TEXT,'霍格沃兹测试学院')
    WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(element))
    self.driver.find_element(*element).click()
    # 使用css定位，比link更好用
    self.driver.find_element(By.CSS_SELECTOR, ".topic:nth-child(1) .title a").click()

  def test_switch(self):  #切换窗口
    self.driver.get('https://testerhome.com/topics/21805')
    self.driver.find_element(By.LINK_TEXT,'第六届中国互联网测试开发大会').click()
    print(self.driver.window_handles)
    #切换窗口
    self.driver.switch_to.window(self.driver.window_handles[1]) #不是self.driver.switch_to_window
    self.driver.find_element(By.LINK_TEXT,'立即报名').click()

  def test_JS(self):
    for code in [
      # 获取网页标题
      'return document.title',
      # 获取性能数据
      'return JSON.stringify(performance.timing)',
      ''
    ]:
      result = self.driver.execute_script(code)
      print(result)
  
  def test_MTSC2020(self):
    self.driver.find_element(By.LINK_TEXT,'MTSC2020 中国互联网测试开发大会议题征集').click()
    self.driver.find_element(By.CSS_SELECTOR,'.btn-default .caret').click()
    self.driver.find_element(By.LINK_TEXT,'征集议题范围').click()
