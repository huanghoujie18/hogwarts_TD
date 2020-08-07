import requests
from test_requests.api.wework1 import WeWork
from test_requests.api.base_api1 import BaseApi

class Tag:
    # 获取token
    secret='oKPwlYZ2bMunvnI4q6ZDr94YYZc_a4OxH2KM3oEh82k'
    # 需要调用wework模块的get_token方法
    token=WeWork.get_token(secret)
    params={'access_token':token}

    # 创建标签
    def create_tag(self,tagname,tagid):
        url='https://qyapi.weixin.qq.com/cgi-bin/tag/create'
        data={'tagname':tagname,'tagid':tagid}
        r=requests.post(url,params=self.params,json=data)
        return r.json()

    # 获取标签列表
    def get_tag(self):
        url='https://qyapi.weixin.qq.com/cgi-bin/tag/list'
        r=requests.get(url,params=self.params)
        return r.json()

    # 更新标签名字
    def update_tag(self,tagid,tagname):
        url='https://qyapi.weixin.qq.com/cgi-bin/tag/update'
        data={"tagid": tagid,"tagname": tagname}
        r=requests.post(url,params=self.params,json=data)
        return r.json()

    # 删除标签
    def delete_tag(self,tagid):
        url='https://qyapi.weixin.qq.com/cgi-bin/tag/delete'
        data={'tagid':tagid}
         # 使用字典(Dictionary) update()方法更新params
        self.params.update(data)
        r=requests.get(url,params=self.params)
        return r.json()

    # 获取标签成员，传入tagid获取对应的标签信息
    def get_member_tag(self,tagid):
        data={'tagid':tagid}
        self.params.update(data)
        url='https://qyapi.weixin.qq.com/cgi-bin/tag/get'
        r=requests.get(url,params=self.params)
        return r.json()


    # 增加标签成员
    url='https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers'


    # 删除标签成员
    url='https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers'





