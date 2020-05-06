# 测试toast控件，使用app是appium官方提供的演练API Demos。
'''
toast不属于app的控件，而是属于android的系统控件，必须使用xpath查找，//*[@class='android.widget.Toast']
'''
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestToast:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        # caps["noReset"] = True
        # caps["dontStopAppOnReset"] = True
        # caps["unicodeKeyboard"] = True
        # caps["resetKeyboard"] = True
        caps["skipServerInstallation"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located())

    def test_toast(self):
        self.driver.find_element(By.XPATH,"//*[@text='Views']").click()
        # 滚动查找，直到查找到Popup Menu点击
        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
                'new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView('
                    'new UiSelector().text("Popup Menu").instance(0));')
        self.driver.find_element(*scroll_to_element).click()
        # 页面上看到文本是“AKE A POPUP!”，直接使用此文本查找报错，通过uiautomatorviewer可以看到是"Make a Popup!"
        # self.driver.find_element(By.XPATH, "//*[@text='MAKE A POPUP!']").click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Make a Popup!").click()  # ACCESSIBILITY_ID是定位resource-id
        self.driver.find_element(By.XPATH, "//*[@text='Search']").click()
        # toast定位
        toast=self.driver.find_element(By.XPATH, "//*[@class='android.widget.Toast']").text
        assert "Search" in toast
        assert "Clicked" in toast

    def teardown(self):
        pass
        # sleep(20)
        # self.driver.quit()
