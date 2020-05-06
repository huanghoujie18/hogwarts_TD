from selenium.webdriver.common.by import By
from test_selenium.page.base_page import BasePage
from test_selenium.page.register import Register


class Login(BasePage):
    def login(self):
        pass

    def to_register(self):
        # 点击注册
        self.driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return Register(self.driver)
