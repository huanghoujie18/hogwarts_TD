from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    base_url = ''

    def __init__(self, dvier: WebDriver = None):
        if dvier is None:
            self.driver = webdriver.Chrome()
        else:
            self.driver = dvier
        self.driver.implicitly_wait(5)
        if self.base_url != '':
            self.driver.get(self.base_url)

    def close(self):
        sleep(5)
        self.driver.quit()
