import requests

from test_requests.api.base_api import BaseApi


class WeWork(BaseApi):
    # 每个企业微信corpid是唯一的，设置为类变量
    corpid = 'ww0ff069f77ced0d7a'
    @classmethod   # 设置为类方法，不需要实例化就可以使用
    # 获取token，个应用都需要获取token，所以抽取出来
    def get_token(cls, secret):  # 每个应用的secret都不同，所以设置为变量
        base_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params = {'corpid':cls.corpid, 'corpsecret':secret}
        r = requests.get(base_url,params=params)
        # 提取出access_token
        return r.json()['access_token']
