from time import sleep
from selenium import webdriver  # driver需要的依赖
from selenium.webdriver.common.by import By  # 元素定位

class TestBiying:
    # 做初始化的操作
    def setup_method(self):
        self.driver = webdriver.Chrome()  # 实例化webdriver对象
        self.driver.get('https://baidu.com/')  # 打开url
        #隐式等待
        self.driver.implicitly_wait(5)

    # 做收尾操作
    def teardown_method(self):
        # 等待3秒
        sleep(3)  # from time import sleep
        # 退出浏览器
        self.driver.quit()

    # 放测试步骤
    def test_baidu(self):
        # 需要导入from selenium.webdriver.common.by import By
        self.driver.find_element(By.ID, "kw").click()
        self.driver.find_element(By.ID, "kw").send_keys("selenium")
        self.driver.find_element(By.ID, "su").click()
        self.driver.find_element(By.CSS_SELECTOR,)
        self.driver.find_element_by_css_selector()
        # 元素定位，有id、name，优先使用id、name定位，id是唯一的。

