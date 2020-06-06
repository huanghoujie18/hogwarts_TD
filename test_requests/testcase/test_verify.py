import requests
def test_verify():
    # 以携程为例
    url='https://www.ctrip.com/'
    r=requests.get(url=url,verify=False)
    print(r.text)
