import json

import yaml
from jsonpath import jsonpath


class BaseApi():
    @classmethod  # 定义为类方法 ，无需实例化便可使用
    def format(cls,r):
        print(json.dumps(r.json(), indent=2,ensure_ascii=False))

    # jsonpath的封装，1.省掉每次import，2.省掉r
    @classmethod
    def jsonpath(cls,r,path):
        return jsonpath(r,path)

    # 封装yaml文件的加载
    @classmethod
    def yaml_load(cls,path) -> list:
        with open(path) as  f:
            return yaml.safe_load(f)

