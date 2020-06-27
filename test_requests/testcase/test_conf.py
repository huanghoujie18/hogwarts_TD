import requests
from config.conf import * # 从config导入

def test_conf():
    # url=server_ip()+'login'  # server_ip()代表函数，而不是调用函数。+ 拼接
    url=server_ip()
    print(url)
    r=requests.get(url=url)
    print(r.text)
    assert 1==1
