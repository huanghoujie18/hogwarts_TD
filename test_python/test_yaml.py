import yaml
# 从test_requests.api.base_api1导入BaseApi类
from test_requests.api.base_api1 import BaseApi
def test_yaml():
    with open('../test_python/yaml_data.yaml',encoding='utf-8') as f:
        print("使用：encoding='utf-8'")
        print(yaml.safe_load(f))
    # {'companies': [{'id': 1, 'name': 'company1', 'price': '200W'}, {'id': 2, 'name': 'company2', 'price': '500W'}]}

    # 以二进制格式打开一个文件用于只读
    with open('../test_python/yaml_data.yaml','rb') as f:
        print("使用：'rb'")
        print(yaml.load(f))

def test_yaml2():
    with open('../test_python/yaml_data2.yaml',encoding='utf-8') as f:
        print("使用：encoding='utf-8'")
        print(yaml.safe_load(f))

def test_yaml3():
     with open('../test_python/yaml_data3.yaml',encoding='utf-8') as f:
        print("使用：encoding='utf-8'")
        print(yaml.safe_load(f))
     # yaml文件需要有空格，不然报错：yaml.scanner.ScannerError: mapping values are not allowed here

def test_yaml4():
     with open('../test_python/yaml_data4.yaml',encoding='utf-8') as f:
        print("使用：encoding='utf-8'")
        print(yaml.safe_load(f))
        # {'create': [{'name': 'demo1', 'age': 30}, {'token': 'accesstoekn'}]}

def test_yaml5():
     with open('../test_python/yaml_data5.yaml',encoding='utf-8') as f:
        print("使用：encoding='utf-8'")
        print(yaml.safe_load(f))
        # [{'create': [{'name': 'demo1', 'age': 30}, {'token': 'accesstoekn'}]}]



