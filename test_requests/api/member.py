import requests

from test_requests.api.wework1 import WeWork
from test_requests.api.base_api1 import BaseApi


# 通讯录管理-成员管理
class Member():
    # 先获取token，成员管理还是再通讯录管理下，跟部门管理需要的token一样
    secret = 'oKPwlYZ2bMunvnI4q6ZDr94YYZc_a4OxH2KM3oEh82k'
    params = {'access_token': WeWork.get_token(secret)}

    # 创建成员
    def create(self, userid, name, email, department, **kwargs):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {'userid': userid, 'name': name, 'email': email, 'department': department}
        data.update(kwargs)  # 不能用 data = data.update(kwargs)
        r = requests.post(url, params=self.params, json=data)
        return BaseApi.format(r)

    def create_one(self,userid,name,email):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": userid,
            "name": name,
            "department": [1, 2],    # todo 如何传入参数？  *解包
            "email": email+"@sqmcdkjwwgc.onexmail.com",   # 拼接字符串
            "is_leader_in_dept": [1, 0],
            "enable": 1,
            "main_department": 1
        }

        r = requests.post(url, params=self.params, json=data)
        return BaseApi.format(r)

    # 获取成员
    def get(self, userid):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        params = {'access_token': WeWork.get_token(self.secret), 'userid': userid}
        r = requests.get(url, params=params)
        return r.json()

    # 更新成员
    def update(self, userid, alias):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {'userid': userid, 'alias': alias}
        r = requests.post(url, params=self.params, json=data)
        return r.json()

    # 删除成员，成员UserID为必填项，使用get方法
    def delete(self, userid):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        params = {'access_token': WeWork.get_token(self.secret), 'userid': userid}
        r = requests.get(url, params=params)
        return r.json()

    # 批量删除成员
    def batchdelete(self, *userid):  # 星号（*）在形参中的作用是“打包”
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete'
        #   请求体{"useridlist": ["zhangsan", "lisi"]}，成员UserID列表
        data = {"useridlist": [*userid]}  # 星号（*）在实参中的作用是“解包”
        r = requests.post(url, params=self.params, json=data)
        return r.json()
