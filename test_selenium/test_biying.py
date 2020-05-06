from time import sleep
from selenium import webdriver  # driver需要的依赖
from selenium.webdriver.common.by import By  # 元素定位


class TestBiying:
    # 做初始化的操作
    def setup_method(self):
        self.driver = webdriver.Chrome()  # 实例化webdriver对象
        self.driver.get('https://cn.bing.com/')  # 打开url
        #隐式等待
        self.driver.implicitly_wait(5)

    # 做收尾操作
    def teardown_method(self):
        # 等待3秒
        sleep(3)  # from time import sleep
        # 退出浏览器
        self.driver.quit()

    # 放测试步骤
    def test_biying(self):
        # 需要导入from selenium.webdriver.common.by import By
        ele = self.driver.find_element(By.ID, 'sb_form_q')   #返回一个页面对象。精简代码的思想。
        ele.click()  #有可能要先定位到输入框，才可以输入
        ele.clear()  #清除原有的内容
        ele.send_keys('selenuim')
        # 元素定位，有id、name，优先使用id、name定位，id是唯一的。
        self.driver.find_element(By.ID, 'sb_form_go').click()
