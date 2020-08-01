import json

import jsonpath
import requests
import yaml


class BaseApi:
    params = {}  # todo 这是空的，send_api怎么循环？其他地方调用send_api时，首先给其赋值

    # 传入yaml文件路径，加载yaml文件
    @staticmethod
    def yaml_load(path):
        with open(path) as f:
            return yaml.safe_load(f)

    def json_path(self,path,r=None):
        if r is None:
            r=self.r
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
        # 进行替换，把key替换为value
        for key, value in self.params.items():
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
        self.format(result)
        return result.json()  # 注意返回json，否则会报错：TypeError: 'Response' object is not subscriptable
