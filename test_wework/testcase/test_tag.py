from test_wework.api.tag import Tag


class TestTag:

    def setup_class(self):
        self.tag = Tag()

    def test_get(self):
        self.tag.get()

    def test_add(self):
        self.tag.add_tag('test005')  # 使用add命名方法有问题，估计重名了
        self.tag.get()

    def test_delete(self):
        # self.tag.add('test002')
        self.tag.get()
        # 添加之后断言：test002在标签里面
        self.tag.delete(1)
        # 删除后断言：test002不在标签里面
        self.tag.get()

    def test_update_tag(self):
        self.tag.update_tag(2,'修改后的标签名')
        self.tag.get()
