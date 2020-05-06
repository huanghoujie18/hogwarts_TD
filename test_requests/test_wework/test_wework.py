import requests
import json


class TestWeWork:
    token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    corpid = 'ww0ff069f77ced0d7a'
    # 自建应用“测试部”的secret
    # secret = 'N7Ni0rynm_CrusreNrdQimX-9C2CCXvizpPi9Q9ocJU'
    # 客户联系引用的secret
    secret = 'GAZo9iiHBZ9Aa2vkb-1xZqLGOWYInEGQ6YBmIUHlgPs'
    token = None
    @classmethod
    def setup(cls):
        r=requests.get(cls.token_url,params={'corpid':cls.corpid,'corpsecret':cls.secret})
        assert r.json()['errcode'] == 0
        cls.token = r.json()['access_token']

    def test_token(self):
        print(self.token)
        assert self.token != None

    # 获取客户群列表
    def test_groupchat_get(self):
        list_url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list'
        r=requests.post(list_url,
                        params={"access_token":self.token},
                        json={"offset": 0,"limit": 100}
                        )
        print(r.json())

    # 获取客户群详情
    def  test_groupchat_detail(self):
         # 首先要获取chat_id
         list_url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list'
         r=requests.post(list_url,
                        params={"access_token":self.token},
                        json={"offset": 0,"limit": 100}
                        )
         chat_id=r.json()["group_chat_list"][0]["chat_id"]
         # 获取客户群详情
         detail_url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/get'
         r=requests.post(detail_url,
                         params={"access_token":self.token},
                        json={"chat_id": chat_id}
                         )
         print(r.json())
         # 格式化打印json报文，indent表示缩进
         print(json.dumps(r.json(), indent=2))
         # 断言成员列表大于0，判断已经获取到客户群
         assert len(r.json()["group_chat"]["member_list"]) > 0
