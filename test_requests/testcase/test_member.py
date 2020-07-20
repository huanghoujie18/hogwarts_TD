from test_requests.api.member import Member


class TestMember():
    member = Member()  # todo 需要优化，不要每次调用方法都实例化，这个测试类只需要实例化一次就好了

    def test_create(self):
        r = self.member.create("test001", "传说", "zhangsan@gzdev.com",1)
        print(r)
        # 错误说明:成员name参数不合法   API错误码:60112

    def test_create_one(self):  #todo 参数化
        r = self.member.create_one()
        print(r)

    def test_get(self):
        r = self.member.get('HuangHouJie')
        print(r)

    def test_update(self):
        r = self.member.update('HuangHouJie', '捷后愚生')
        print(r)

    def test_delete(self):
        r = self.member.batchdelete('test001')
        print(r)
        assert r["errmsg"] == "deleted"

    def test_batchdelete(self):
        r = self.member.batchdelete('test001')
        print(r)
        assert r["errmsg"] == "deleted"
