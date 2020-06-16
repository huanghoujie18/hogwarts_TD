from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestHome():
    def setup(self):
        # 使用Options，需要from selenium.webdriver.chrome.options import Options
        chromeOptions = Options()
        #9222是端口号，只要是不被占用的端口号都可以
        chromeOptions.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
        # 使用webdriver，需要from selenium import webdriver
        self.driver = webdriver.Chrome(options=chromeOptions)
        # 隐式等待，是全局生效的
        self.driver.implicitly_wait(3)

    def teardown(self):
        sleep(5)  # from time import sleep
        self.driver.quit()

    def test_home(self):
        self.driver.find_element(By.ID, 'menu_contacts').click()  # 使用By，需要from selenium.webdriver.common.by import By
        # self.driver.find_element_by_id('menu_contacts').click()
        # sleep(2)
        # 显式等待
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member')))

        # self.driver.find_element(By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member').click()

        # 循环去点击“添加成员”按钮
        WebDriverWait(self.driver, 10).until(self.wait_element)  # 不是WebDriverWait(self.driver,10).until(self.wait_element())

        '''
        while True:
            self.wait_element()
            
        '''
        self.driver.find_element(By.ID, 'username').send_keys('Tom')
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys('Tom111')
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys('13838383388')
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()

    # 根据页面是否有“姓名”输入框，判断页面是否已经跳转到录入信息页面
    def wait_element(self, x):  # 复用until方法，所以得加x。其实还不明白
        size = len(self.driver.find_elements(By.ID, 'username'))  # 调用这个方法时，self.driver.find_elements也会受到隐式等待的影响
        if size < 1:
            self.driver.find_element(By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member').click()
        return size >= 1
