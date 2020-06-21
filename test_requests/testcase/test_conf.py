import requests
from config.conf import * # 从config导入

def test_conf():
    url=server_ip()+'/login'  # 
    print(url)
    r=requests.get(url=url)
    print(r.text)
