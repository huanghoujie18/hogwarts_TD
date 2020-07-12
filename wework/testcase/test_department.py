
from wework.department import Department


class Test_department:
    # department=Department() 为何在这里实例化，方法中不能调用
    def test_get_department(self):
        r=Department().get_department()
        # print(r)
        assert r['errcode']==0

    def test_create_department(self):
        r=Department().create_department()
        # print(r)
        assert r['errcode']==0

    def test_update_department(self):
        r=Department().update_department()
        # print(r)
        assert r['errcode']==0

    def test_delete_department(self):
        r=Department().delete_department()
        print(r)
        assert r['errcode']==0
