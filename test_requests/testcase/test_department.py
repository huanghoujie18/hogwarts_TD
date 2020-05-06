from test_requests.api.base_api import BaseApi
from test_requests.api.department import Department
from test_requests.api.wework import WeWork


class TestDepartment(BaseApi):
    def setup(self):
        self.department = Department()  # 需要先实例化，才可调用Department类中的方法
        self.baseapi = BaseApi()

    def test_token(self):
        # 测试获取token
        r = WeWork.get_token('oKPwlYZ2bMunvnI4q6ZDr94YYZc_a4OxH2KM3oEh82k')  # 直接调用WeWork类下的方法，不需要实例化
        assert r['errmsg'] == 'ok'
        # self.format(r)
        # todo 继承在子类中如何调用父类中的方法，没有调用成功

    def test_create(self):
        r = self.department.create('abcd', 1)
        assert r['errmsg'] == 'created'
        print(r)

    def test_update(self):
        r = self.department.update(5, '修改后的部门名称')
        assert r['errmsg'] == 'updated'
        print(r)

    def test_delete(self):
        r = self.department.delete(5)
        assert r['errmsg'] == 'deleted'
        print(r)

    def test_get(self):
        r = self.department.get()
        assert 'abcd' not in r
        print(r)
