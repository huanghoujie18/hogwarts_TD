import requests
from requests import Session

# 获取响应结果
def test_requests():
    r = requests.get('https://www.baidu.com')
    print('\n')
    print('状态码是：', r.status_code)
    print('url是：', r.url)
    print('头信息是：', r.headers)
    print('cookies是：', r.cookies)
    print('text是：', r.text)
    print('请求是：', r.request)


# get请求带query参数 ，为 URL 的查询字符串(query string)传递某种数据
def test_get():
    r = requests.get("https://httpbin.testing-studio.com/get",
                     params={
                         'a': 1,
                         'b': 2,
                         'c': 'asd'
                     })
    print(r.json())


# post请求带form表单
def test_post():
    r = requests.post('https://httpbin.testing-studio.com/post',
                      data={'a': 1,
                            'b': '[1,2,3]',
                            'c': 'aqwe'},
                      # 构造请求头
                      headers={'h': 'headersdemo'},
                      cookies={'c': 'cookiesdemo'}
                      )
    print(r.json())


# 上传文件
def test_upload():
    r = requests.post(
        'https://httpbin.testing-studio.com/post',
        files={'file': open('__init__.py', 'rb')}
    )
    print(r.json())
    assert r.status_code == 200

# 代理机制
proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}
def test_proxies():
    r = requests.get("https://httpbin.testing-studio.com/get",
                     # get请求带query参数 ，为 URL 的查询字符串(query string)传递某种数据
                     params={
                         'a': 1,
                         'b': 2,
                         'c': 'asd'
                     },
                     proxies=proxies,
                     verify=False  # 关闭校验，否则代理无法抓包
                     )

    print(r.json())

# session机制
def test_seesion():
    s=Session()
    s.headers={'h':'test_headers'}
    r=s.post('https://httpbin.testing-studio.com/post',data={'a':1})
    print(r.json())

# hook机制，修改响应返回的内容，或替换响应返回的内容
def test_get_hook():
    def hook(r,*args,**kwargs):
        r.demo = 'demo content'
    r = requests.get("https://httpbin.testing-studio.com/get",
                     params={
                         'a': 1,
                         'b': 2,
                         'c': 'asd'
                     },
                     hooks={'response': [hook]}
                     )
    print(r.json())
    print(r.demo)
