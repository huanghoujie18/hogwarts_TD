# 测试用例
from test_selenium.page.index import Index

class TestIdex:
    # 测试注册
    def setup(self):
        self.index = Index()
    # 从主页入口测试注册
    def test_register(self):
        self.index.go_to_register().register('东印度公司','莱克星顿','13838383388')
    # 从企业登录入口测试注册
    def test_login(self):
        register_page = self.index.goto_login().goto_register().register('环太平洋公司','戴比尔斯','15655666655')
        # 断言
        print(register_page.get_error_message())
        # 判断“请选择”是否在获取的错误信息里
        assert '请选择' in "|".join(register_page.get_error_message())
    def teardown(self):
        self.index.close()
