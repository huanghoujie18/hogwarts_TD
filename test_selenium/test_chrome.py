# 从selenium导入webdriver,后面的依赖都是在selenium.webdriver下
from selenium import webdriver
# 从selenium.webdriver.options导入Options
from selenium.webdriver.chrome.options import Options
#从selenium.webdriver.common.by导入By
from selenium.webdriver.common.by import By

# 复用已打开的浏览器
class TestChrome:
    def setup(self):
        # 实例化对象
        chromeOptions = Options()
        #先在cmd中用命令行chrome --remote-debugging-port=9222打开浏览器，添加复用的浏览器
        chromeOptions.add_experimental_option('debuggerAddress','127.0.0.1:9222')  #名称一定是debuggerAddress
        #把复用浏览器给driver
        self.driver = webdriver.Chrome(options=chromeOptions)
        self.driver.implicitly_wait(3)
    def test_chrome(self):
        self.driver.find_element(By.LINK_TEXT,'企业注册').click()

