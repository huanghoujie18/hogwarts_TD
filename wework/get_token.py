import requests

'''
获取access_token是调用企业微信API接口的第一步，相当于创建了一个登录凭证，其它的业务API接口，都需要依赖于access_token来鉴权调用者身份。
因此开发者，在使用业务接口前，要明确access_token的颁发来源，使用正确的access_token。
corpid，每个企业都拥有唯一的corpid，获取此信息可在管理后台“我的企业”－“企业信息”下查看“企业ID”。   ww0ff069f77ced0d7a
secret，是企业应用里面用于保障数据安全的“钥匙”，每一个应用都有一个独立的访问密钥。
通讯录secret:	oKPwlYZ2bMunvnI4q6ZDr94YYZc_a4OxH2KM3oEh82k
'''
# 获取access_token
def get_token(corpsecret):
     url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
     params={'corpid':'ww0ff069f77ced0d7a','corpsecret':corpsecret}
     r=requests.get(url,params=params)
     return r.json()['access_token']
