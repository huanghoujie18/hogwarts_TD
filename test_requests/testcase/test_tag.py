import jsonpath

from test_requests.api import tag
from test_requests.api.tag import Tag


class TestTag:

    @classmethod
    def setup_class(cls):
        # 实例化对象
        cls.tag = Tag()

    # 创建一个不存在的标签
    def test_create_tag(self):
        r = self.tag.create_tag('tag1000', 1000)
        print(r)

    def test_create_tag_fail(self):
        r = self.tag.create_tag('tag1000', 1000)
        # 断言API错误码40068
        assert r['errcode'] == 40068

    def test_get_tag(self):
        r = self.tag.get_tag()
        print(r)

    def test_update_tag(self):
        # 首先修改一个标签的id和name
        r = self.tag.update_tag(3, '修改标签名称')
        # 接着进行断言
        assert r["errmsg"] == "updated"
        # 然后把标签的id和name修改为原来的值\
        r = self.tag.update_tag(3, '复原标签名称')
        # 最后进行断言
        assert r["errmsg"] == "updated"

    def test_delete_tag(self):
        # 首先添加一个新的标签
        r = self.tag.create_tag('tag10000', 10000)
        # 接着断言标签在列表中
        r = self.tag.get_tag()
        assert 'tag10000' in jsonpath.jsonpath(r, '$..tagname')
        # 然后删除标签
        r = self.tag.delete_tag(10000)
        # 最后进行断言标签已经不再列表中
        r = self.tag.get_tag()
        assert 'tag10000' not in jsonpath.jsonpath(r, '$..tagname')

    def test_get_member_tag(self):
        r=self.tag.get_member_tag(4)
        assert r['tagname']=='test005'
