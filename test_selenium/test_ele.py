from selenium import webdriver
from time import ctime, sleep
from selenium.webdriver.chrome.options import Options
# 想练习不同元素定位，没成功。微信注册有下拉框
class TestEle:
    def setup_method(self):
        chromeOptions = Options()
        chromeOptions.add_experimental_option('debuggerAddress','127.0.0.1:9222')
        self.driver = webdriver.Chrome(options=chromeOptions)
        # self.driver.get('https://i.51job.com/userset/my_51job.php')
        self.driver.implicitly_wait(5)
    def test_ele(self):
        self.driver.find_element_by_link_text('编辑').click()
    def teardown_method(self):
        sleep(3)
        # self.driver.quit()
