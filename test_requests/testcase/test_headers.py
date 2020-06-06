import requests
def test_51job():
    # 前程无忧搜索岗位不需要headers信息
    url='https://search.51job.com/list/030200,000000,0000,00,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    r_51job=requests.get(url=url)
    # print(r_51job.text)
    print(r_51job.encoding)  # html默认的编码方式是ISO-8859-1
    r_51job.encoding='gb2312' # 修改编码方式
    print(r_51job.text)
def test_12306():
    # 12306搜索车票需要添加headers信息，只需要cookies即可。实际工作中，headers需要哪些值，咨询开发人员了解。
    url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-06-06&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=GZQ&purpose_codes=ADULT'
    headers={'Cookie': 'JSESSIONID=C5DCA622147CEF2C4D9C3D3E53E9CF26; BIGipServerotn=1406730506.64545.0000; RAIL_EXPIRATION=1591740743186; RAIL_DEVICEID=FqtrEO_1lQCMdLmY_0uxjBNyLf5esH-V-KtA_I-kPu0j721_HYTxo4IobbdtZbAr75fLtGhLHAQTE8mWEaNmM7ococf3hUVIFw-Gaaper7CzwlrDFsHwwey8w_YQ5gGoMoyfKgVJ5o4nNuWVYhuiC_cxPzsWFJkF; BIGipServerpassport=954728714.50215.0000; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_toStation=%u5E7F%u5DDE%2CGZQ; _jc_save_fromDate=2020-06-06; _jc_save_toDate=2020-06-06; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u4E0A%u6D77%2CSHH'}
    r_12306=requests.get(url=url,headers=headers)
    print(r_12306.text)
