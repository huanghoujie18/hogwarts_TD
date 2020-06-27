# 动态关联
import requests
import re  # 正则表达式库，python自带的库

def test_cookies():
    # 以百度为例
    r_baidu=requests.get('https://www.baidu.com/')
    print(r_baidu.cookies)

def test_text():
    # 返回响应是text格式，使用正则表达式提取其中的值，以前程无忧为例，前程无忧搜索不需要cookies，不需要headers
    url_51='https://search.51job.com/list/030200,000000,0000,00,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    r_51=requests.get(url=url_51)  #前程无忧搜索不需要cookies，不需要headers
    r_51.encoding='gb2312'  # 设置编码格式，不然会乱码
    # print(r_51.text)
    # "广州通易科技有限公司" href="https://jobs.51job.com/all/co727220.html">广州通易科技有限公司，把url提取出来
    url_ty=re.findall('title="广州通易科技有限公司" href="(.+?)">广州通易科技有限公司',r_51.text)
    print(url_ty[0])
    # 访问新的url
    r_ty=requests.get(url=url_ty[0])  # 提取出来的是列表，所以取第一个
    r_ty.encoding='gb2312'
    print(r_ty.text)
    # requests.exceptions.ConnectionError: ('Connection aborted.', ConnectionResetError(10054, '远程主机强迫关闭了一个现有的连接。', None, 10054, None))

def test_url():
    url='https://jobs.51job.com/all/co727220.html'
    r=requests.get(url=url)  # 似乎不能直接访问跳转的链接
    print(r.text)

# 以12306为例
def test_json():
    url_12306='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-06-27&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=GZQ&purpose_codes=ADULT'
    headers={'Cookie': 'JSESSIONID=84073130E457BB033010951BC41B3625; _jc_save_toStation=%u5E7F%u5DDE%2CGZQ; _jc_save_wfdc_flag=dc; BIGipServerotn=1373176074.24610.0000; RAIL_EXPIRATION=1593576175962; RAIL_DEVICEID=PbasnpR7ZB2Xcn9qUnd7wNs2_SVXfMI4i5jkkwMKc9BZi1gUKxv7l2uVortBg0YoV8db3y9eOoQx8m7JX1lO1lKwdkOjAS-b5je341esn7o7ct1GPA1WWVshf_Z4kzUi_Ns6JXJc-yyxBq3GYBurzp4HiFl8P7hR; BIGipServerpassport=937951498.50215.0000; route=c5c62a339e7744272a54643b3be5bf64; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_fromDate=2020-06-27; _jc_save_toDate=2020-06-27'}
    r_12306=requests.get(url=url_12306,headers=headers)
    print(r_12306.json())
    print(r_12306.json()['httpstatus'])
    print(r_12306.json()['data']['map'])
    print(r_12306.json()['data']['map']['BXP'])
    origin=r_12306.json()['data']['map']['BXP']
