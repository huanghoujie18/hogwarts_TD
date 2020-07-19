import requests
from test_requests.api.base_api1 import BaseApi


class TestBaseApi():
    def test_format(self):
        url =  'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        corpid = 'ww0ff069f77ced0d7a'
        secret = 'oKPwlYZ2bMunvnI4q6ZDr94YYZc_a4OxH2KM3oEh82k'
        params = {'corpid':corpid, 'corpsecret':secret}     # 注意：不用self.corpid
        r = requests.get(url,params=params)
        BaseApi.format(r)      # 调用base_api1的format方法
