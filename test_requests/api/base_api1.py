import json

class BaseApi():
    @classmethod  # 定义为类方法 ，无需实例化便可使用
    def format(cls,r):
        print(json.dumps(r.json(), indent=2))
