import pytest
from test_wework.api.tag import Tag


class TestTag:
    def setup_class(self):
        self.tag = Tag()

    def test_get(self):
        self.tag.get()

    # 参数化
    @pytest.mark.parametrize(('tagname,tagid'),[('test099',99),('test100',100)])
    def test_add(self,tagname,tagid):
        self.tag.add_tag(tagname,tagid)  # 使用add命名方法有问题，估计重名了
        self.tag.get()   # 返回的是一个json数据
        # 断言  添加后获取标签列表，判断添加的tagname在列表里面，或者判断taglist的长度大于没添加之前的
        # print(len(r['taglist']))


    # def test_add(self):
    #     self.tag.add_tag('test007',97)  # 直接使用add命名的方法有问题，估计重名了
    #     self.tag.get()

    def test_delete(self):
        # 减少用例依赖，先添加标签，再删除标签
        self.tag.add_tag('test999',999)
        self.tag.get()
        # 添加之后断言：test002在标签里面

        # 根据标签名获取标签id，删除标签时需要传标签id
        # result=self.tag.json_path('$..taglist[?(@.tagname=="test002")]')
        # print(result)
        self.tag.delete(999)
        # 删除后断言：test002不在标签里面
        self.tag.get()

    def test_update_tag(self):
        self.tag.update_tag(2,'修改后的标签名')
        self.tag.get()
