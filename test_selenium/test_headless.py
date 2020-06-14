from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_headless():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1280,1696')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get('https://www.baidu.com/')
    driver.find_element(By.CSS_SELECTOR,'.s_ipt').send_keys('selenium')
    driver.find_element(By.CSS_SELECTOR,'#su').click()
