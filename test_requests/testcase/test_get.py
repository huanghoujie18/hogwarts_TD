import requests
def test_get():
    # 参数保存在url中，?后面添加参数名称和参数值，如果有多个参数，使用&连接
    url = 'http://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=13909161860'
    r=requests.get(url=url)
    print(r.text)
    print(r.status_code)
    print(r.cookies)
    print(r.url)
    # 参数保存在params中，params以字典形式保存数据
    url = 'http://tcc.taobao.com/cc/json/mobile_tel_segment.htm'
    params={'tel':13909161860}
    r=requests.get(url=url,params=params)
    print(r.text)
    print(r.status_code)
    print(r.cookies)
    print(r.url)

