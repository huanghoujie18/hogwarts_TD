import requests

from test_requests.api.wework1 import WeWork
from test_requests.api.base_api1 import BaseApi

class Department(WeWork):
    # 先获取token
    secret = 'oKPwlYZ2bMunvnI4q6ZDr94YYZc_a4OxH2KM3oEh82k'
    params={'access_token':WeWork.get_token(secret)}

    def create(self,name,id,**kwargs):
        url='https://qyapi.weixin.qq.com/cgi-bin/department/create'
        data = {'name':name,'parentid':id}  # name id是必填项，其他非必填项参数通过**kwargs接收
        data = data.update(kwargs)  # 如果kwargs有值，则更新data
        r=requests.post(url,params=self.params,json=data)  # 发送创建部门请求
        return BaseApi.format(r)

    def get(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'
        r=requests.get(url,params=self.params)
        return BaseApi.format(r)

    def delete(self,id):
        url='https://qyapi.weixin.qq.com/cgi-bin/department/delete'
        r=requests.get(url,params={'access_token':WeWork.get_token(self.secret),'id':id})
        return BaseApi.format(r)

    def update(self,id,**kwargs):
        url='https://qyapi.weixin.qq.com/cgi-bin/department/update'
        data={'id':id}
        data=data.update(kwargs)
        r=requests.post(url,params=self.params,json=data)
        return BaseApi.format(r)
