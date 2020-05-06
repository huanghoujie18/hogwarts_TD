from test_selenium.page.index import Index

class TestRegister:
    def setup(self):
        # 从首页点击【立即注册】，测试注册。先实例化首页
        self.index = Index()
    def test_register(self):
        # 调用首页Index的goto_register方法进入注册页，进入注册页后调用注册页的register方法
        res = self.index.goto_register().register()
    def test_login(self):
        l = self.index.goto_login().login()
