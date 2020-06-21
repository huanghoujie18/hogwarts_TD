import requests
from common.get_excel import *  #导入自定义的函数
url='https://mubu.com/login/password'
def test_get_excel_row():  #注意：测试用例与定义的的函数在同一
    for i in range(1,get_row()):  #调用get_row()获取文件的总的函数，循环访问
        phone,password=get_excel_row(i)
        params={'phone':phone,'password':password}
        r=requests.get(url=url,params=params)
        print(r.status_code)
        print(r.text)

# def test_dict():   #获取excel文件中字典格式的数据，如{'phone':15625172814,'password':'password123'}
#     params=get_excel_row(4)[0]
#     print(params)
#     print(type(params))  #直接获取是str类型
#     r=requests.get(url=url,params=eval(params))  #使用eval转换类型
#     print(r.status_code)
#     print(r.text)

# 读取excel里的字典数据，如{'phone':15625172814,'password':'password123'}
def test_dict():
    params=get_dict(1)
    print(type(params))  #直接获取是str类型
    print(get_dict(1))
    r=requests.get(url=url,params=eval(get_dict(1)))
    print(r.status_code)
    print(r.text)


