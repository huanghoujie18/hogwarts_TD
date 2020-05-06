# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


class TestSearch:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "Uni"
        caps["noReset"] = True
        caps["skipServerInstallation"] = True  # 提速
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_search(self):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        self.driver.find_element(By.XPATH,
                                 "//*[@resource-id='com.xueqiu.android:id/listview']//*[@text='BABA']").click()
        # 定位“股票”,层级定位
        self.driver.find_element(By.XPATH, "//*[contains(@resource-id,'title_container')]//*[@text='股票']").click()
        # 空间定位，定位兄弟节点，先根据一个子节点找到父节点再定位另一个子节点
        price = (By.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id,'current_price')]")
        assert float(self.driver.find_element(*price).text) < 201
        # 获取属性
        print(self.driver.find_element(*price).get_attribute('resourceId'))

    def test_scroll(self):
        # 获取窗口
        size = self.driver.get_window_size()
        print(self.driver.get_window_size())
        TouchAction(self.driver).long_press(x=size['width'] * 0.5, y=size['height'] * 0.8).move_to(
            x=size['width'] * 0.5, y=size['height'] * 0.2).release().perform()

    def test_devices(self):
        self.driver.background_app(5)
        self.driver.lock(5)
        self.driver.unlock()

    def test_toast(self):

        scroll_to_ele = ()

    def teardown(self):
        self.driver.quit()
