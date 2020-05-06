from selenium.webdriver.common.by import By
from test_selenium.page.base_page import BasePage
from test_selenium.page.login import Login
from test_selenium.page.register import Register


class Index(BasePage):
    base_url = 'https://work.weixin.qq.com/'

    def goto_register(self):
        # 点击注册按钮
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        # 跳转注册页面
        return Register(self.driver)

    def goto_login(self):
        # 点击登录按钮
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        # 跳转登录页面
        return Login(self.driver)
