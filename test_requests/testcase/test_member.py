import pytest

from test_requests.api.member import Member


class TestMember():
    @classmethod
    def setup_class(cls):
        cls.member = Member()  # todo 需要优化，不要每次调用方法都实例化，这个测试类只需要实例化一次就好了

    def test_create(self):
        r = self.member.create("test001", "传说", "zhangsan@gzdev.com",1)
        print(r)
        # 错误说明:成员name参数不合法   API错误码:60112

    @pytest.mark.parametrize(('userid,name,email'),[('test001','test001','test001'),('test002','test002','test002')])
    def test_create_one(self,userid,name,email):  #todo 参数化 值得好好思考
        r = self.member.create_one(userid,name,email)
        print(r)

    # 获取成员
    def test_get(self):
        r = self.member.get('HuangHouJie')
        # print(r)
        assert r['userid']=='HuangHouJie'

    def test_update(self):
        r = self.member.update('HuangHouJie', '捷后愚生')
        # print(r)
        get_member = self.member.get('HuangHouJie')
        # print(get_member)
        assert  get_member['alias'] == '捷后愚生'  #  get_member是 'dict'
        # 把昵称置空
        r = self.member.update('HuangHouJie', ' ')
        get_member = self.member.get('HuangHouJie')
        # print(get_member)
        assert  get_member['alias'] == ' '

        # todo 断言一个字段在json内

    def test_delete(self):
        r = self.member.delete('test001')
        print(r)
        assert r["errmsg"] == "deleted"

    def test_batchdelete(self):
        r = self.member.batchdelete('test001','test002')
        print(r)
        assert r["errmsg"] == "deleted"
