from test_requests.api.wework import WeWork
import requests

class Department(WeWork):
    secret = 'oKPwlYZ2bMunvnI4q6ZDr94YYZc_a4OxH2KM3oEh82k'
    params={'access_token':WeWork.get_token(secret)}
    # 创建部门
    def create(self,name,id,**kwargs):
        data = {'name':name,'parentid':id}
        # data = data.update(kwargs)
        base_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create'
        r = requests.post(base_url,params=self.params,json=data)
        return r.json()['id']
    # 修改部门
    def update(self,id,name):
        base_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/update'
        data = {"id": id,"name": name}
        r = requests.post(base_url,params=self.params,json=data)
        return r.json()
    # 删除部门
    def delete(self,id):
        base_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete'
        r = requests.get(base_url,params={'access_token':WeWork.get_token(self.secret),'id':id})
        return r.json()
    # 查询部门
    def get(self):
        base_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'
        r = requests.get(base_url,params=self.params)
        return r.json()




