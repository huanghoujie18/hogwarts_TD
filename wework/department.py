import requests
from wework.get_token import get_token


class Department:
    corpsecret = 'oKPwlYZ2bMunvnI4q6ZDr94YYZc_a4OxH2KM3oEh82k'

    # 获取token
    access_token = get_token(corpsecret)

    # 获取部门信息
    def get_department(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'
        r = requests.get(url, params={'access_token': self.access_token})
        return r.json()

    # 创建部门
    def create_department(self):
        url='https://qyapi.weixin.qq.com/cgi-bin/department/create'
        data = {
            "name": "测试",
            # "name_en": "TS",
            "parentid": 1,
            # "order": 2
        }
        # 非必须项"id"，如果不填参数，请求时就不要带这个参数
        r = requests.post(url, params={'access_token': self.access_token},json=data)
        return r.json()

    # 更新部门
    def update_department(self):
        url='https://qyapi.weixin.qq.com/cgi-bin/department/update'
        data = {"id": 5,
                "name_en": "TS001"}
        r = requests.post(url, params={'access_token': self.access_token},json=data)
        return r.json()

    # 删除部门
    def delete_department(self):
        url='https://qyapi.weixin.qq.com/cgi-bin/department/delete'
        r = requests.post(url, params={'access_token': self.access_token,'id':5})
        return r.json()
