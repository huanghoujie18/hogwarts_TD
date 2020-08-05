import json
from jsonpath import jsonpath
import requests
import yaml


class BaseApi:
    params = {}  # 这是空的，其他地方调用send_api时，首先给其赋值

    # 传入yaml文件路径，加载yaml文件
    @staticmethod
    def yaml_load(path):
        with open(path,'rb') as f:    # 加上'rb'，避免编码报错
            return yaml.safe_load(f)

    # jsonpath，从json数据中取值，path的json表达式，r是返回的数据
    def json_path(self,path,r=None):
        if r is None:
            r=self.r.json()
        return jsonpath(r,path)

    # 格式化打印方法
    @classmethod
    def format(cls, r):
        cls.r = r.json()  # todo ?
        # 注意json.load与json.loads的区别
        result = json.dumps(json.loads(r.text),indent=2,ensure_ascii=False)
        print(result)
        return result

    # 发送接口报文方法
    def send_api(self, data: dict):
        # 将python对象转成yaml（理解为就是字符串）
        raw = yaml.dump(data)
        # 逐一进行替换，把key替换为value
        for key, value in self.params.items():   # params定义为类变量，继承BaseApi的类可以直接对其进行赋值
            raw = raw.replace(f'${{{key}}}', repr(value))
        # 反序列化
        data = yaml.load(raw)
        # 使用requests发送请求
        result = requests.request(
            method=data['method'],
            url=data['url'],
            params=data['params'],
            json=data.get('json')  # 使用get方法，在json为空的时候也不会报错
        )
        print(data)
        self.format(result)
        return result.json()  # 注意返回json，否则会报错：TypeError: 'Response' object is not subscriptable
