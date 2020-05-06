from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestMail():
    def setup(self):
        self.driver = webdriver.Chrome()

    def test_window(self):
        self.driver.get('https://testerhome.com/topics/21805')
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_link_text('第六届中国互联网测试开发大会').click()
        # 打印窗口，可以观察到出现了多个窗口
        print(self.driver.window_handles)
        # 切换窗口
        self.driver.switch_to.window(self.driver.window_handles[1])
        ele = (By.LINK_TEXT,'演讲申请')
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(ele))
        self.driver.find_element(*ele ).click()

        #todo:单选框、复选框、下拉框http://testing51.mikecrm.com/tNk2AoH

 def test_mail(self):
        self.driver.get('https://mail.163.com/')
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_link_text('密码登录').click()
        self.driver.switch_to.frame(1)
        # element=(By.CSS_SELECTOR,'#auto-id-1585054687939')
        # WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(element))
        # self.driver.find_element(*element).click()
        # self.driver.find_element(*element).send_keys('huanghoujie')
        ele_box = self.driver.switch_to.active_element
        ele_box.send_keys("123")

