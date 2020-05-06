import json


class BaseApi:
    # 用于格式化json报文
    def format(self, r):  # r，通过传入
        print(json.dump(r.json(), indent=2))
