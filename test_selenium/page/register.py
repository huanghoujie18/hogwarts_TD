from selenium.webdriver.common.by import By
from test_selenium.page.base_page import BasePage


class Register(BasePage):
    def register(self):
#         填写信息
        self.driver.find_element(By.CSS_SELECTOR,"#corp_name").send_keys('test001')
        return True
