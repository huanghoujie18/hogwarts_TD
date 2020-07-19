import requests

from test_requests.api.base_api1 import BaseApi


class WeWork(BaseApi):
    corpid = 'ww0ff069f77ced0d7a'

    @classmethod
    def get_token(cls,secret):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params={'corpid':cls.corpid,'corpsecret':secret}
        r=requests.get(url,params=params)
        return r.json()['access_token']
