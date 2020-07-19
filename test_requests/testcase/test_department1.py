from test_requests.api.department1 import Department

# 20200719
class TestDepartment():

    department=Department()

    def test_create(self):
        r=self.department.create('测试再测试',1)
        print(r)
        # 报错：部门ID不存在

    def test_get(self):
        r=self.department.get()
        print(r)

    def test_delete(self):
        r=self.department.delete('5')
        print(r)

    def test_update(self):
        # r=self.department.update({'id':'5',"name_en":"RDGZ"})
        r=self.department.update(5)
        print(r)
        # 报错：部门ID不存在

