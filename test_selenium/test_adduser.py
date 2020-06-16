from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
# 企业微信添加用户
def test_adduser():
    # 复用浏览器，企业微信需要扫描，windows系统首先在cmd执行：chrome --remote-debugging-port=9222
    options=Options()
    options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
    driver=webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    # driver.find_element(By.CSS_SELECTOR,'#menu_contacts .frame_nav_item_title').click()
    # 添加用户
    ele=(By.CSS_SELECTOR,'.js_service_list a:nth-child(1) .index_service_cnt_item_title')
    WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable(ele))
    driver.find_element(*ele).click()  # 点击跳转信息填写页面
    driver.find_element(By.CSS_SELECTOR,'#username').send_keys('测试用户')
    driver.find_element(By.CSS_SELECTOR,'#memberAdd_acctid').send_keys('ceshiyonghu')
    driver.find_element(By.CSS_SELECTOR,'#memberAdd_phone').send_keys('13838383388')
    driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()
    # 断言是否添加成功
    size=driver.find_elements(By.CSS_SELECTOR,'[title="测试用户"]')
    assert len(size) == 1

    # 删除用户
    driver.find_element(By.CSS_SELECTOR,'#member_list tr:nth-child(1) .ww_checkbox').click()
    driver.find_element(By.CSS_SELECTOR,'.js_delete').click()
    print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[0])  # 切换窗体
    driver.find_element(By.CSS_SELECTOR,'.ww_dialog_foot .ww_btn_Blue').click()  # 点击确认
    # 断言是否删除成功
    driver.refresh()  # 刷新页面
    size=driver.find_elements(By.CSS_SELECTOR,'[title="测试用户"]')  # 获取页面元素
    assert len(size) == 0

