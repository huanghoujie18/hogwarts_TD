import requests

from test_requests.api.base_api import BaseApi


class WeWork(BaseApi):
    corpid = 'ww0ff069f77ced0d7a'
    @classmethod   # 设置为类方法，不需要实例化就可以使用
    # 每个应用都需要获取token，所以抽取出来
    def get_token(cls, secret):  # 每个应用的secret都不同，所以设置为变量
        base_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params = {'corpid':cls.corpid, 'corpsecret':secret}
        r = requests.get(base_url,params=params)
        return r.json()['access_token']  # 提取出access_token
