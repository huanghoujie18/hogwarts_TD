
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestXueqiu:
    def setup(self):
        # 配置Appium 服务器初始化参数（Capability）
        # 创建一个空字典，然后往里面添加各种值
        caps = {}
        caps["platformName"] = "Android"  # 使用的手机操作系统 iOS, Android
        caps["deviceName"] = "test"  # 使用的手机或模拟器类型，在 Andorid 上虽然这个参数目前已被忽略，但仍然需要添加上该参数
        caps["appPackage"] = "com.xueqiu.android"  # 运行的 Android 应用的包名
        # 使用adb logcat |grep -i displayed获取app入口，如雪球app的入口如下：com.xueqiu.android/.view.WelcomeActivityAlias
        caps["appActivity"] = ".view.WelcomeActivityAlias"  # Activity 的名字是指从你的包中所要启动的 Android acticity。他通常需要再前面添加. （例如 使用 .MainActivity 代替 MainActivity）
        # 每一个页面都是一个activity，简单理解就是指定进入哪个页面
        caps["noReset"] = True  # 在当前 session 下不会重置应用的状态。默认值为 false，每次都重置session
        # caps["fullReset"] = True  # (iOS)删除所有的模拟器文件夹。(Android) 要清除 app 里的数据，请将应用卸载才能达到重置应用的效果。在 Android, 在 session 完成之后也会将应用卸载掉。默认值为 false
        caps["dontStopAppOnReset"] = True  # 在使用 adb 启动应用之前，不要终止被测应用的进程。
        # caps["udid"] = "" # 当有多台设备时，指定连接哪一台设备。可以使用adb devices 指令查看设备
        caps["unicodeKeyboard"] = True  # 使用 Unicode 输入法。 默认值为 false，设置为True可以输入中文
        caps["resetKeyboard"] = True  # 在设定了 unicodeKeyboard 关键字的 Unicode 测试结束后，重置输入法到原有状态。如果单独使用，将会被忽略。默认值为 false
        # 是resetKeyboard，还是resetKeyBoard
        caps["skipServerInstallation"] = True  # 跳过检查和对应用进行 debug 签名的步骤。仅适用于 UiAutomator，不适用于 selendroid。 默认值为 false
        # caps["noSign"] = True
        # 初始化driver
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待
        self.driver.implicitly_wait(20)

    def testSerch(self):
        # self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID,"tv_search").click()     # MobileBy继承By
        # self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID,"search_input_text").send_keys("阿里巴巴")

    def test_getPrice(self):
        self.driver.find_element(MobileBy.ID,"tv_search").click()     # MobileBy继承By
        self.driver.find_element(MobileBy.ID,"search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID,"name").click()
        # 获取价格，转换为float类型进行断言
        assert float(self.driver.find_element(MobileBy.ID, "current_price").text) > 250
        # 不需要写全称，如这样 self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/current_price").text

    def test_xpath(self):
        self.driver.find_element(MobileBy.ID,"tv_search").click()     # MobileBy继承By
        self.driver.find_element(MobileBy.ID,"search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.XPATH,"//*[@text='阿里巴巴' and contains(@resource-id,'name')]").click()
        assert float(self.driver.find_element(MobileBy.ID, "current_price").text) > 250


    def teardown(self):
        self.driver.quit()
