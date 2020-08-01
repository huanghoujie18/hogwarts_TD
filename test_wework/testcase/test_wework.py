from test_wework.api.wework import WeWork
class TestWework:

    # 获取token
    def test_get_tokne(self):
        wework=WeWork()
        r=wework.get_token('oKPwlYZ2bMunvnI4q6ZDr94YYZc_a4OxH2KM3oEh82k')
    # 客户联系：GAZo9iiHBZ9Aa2vkb-1xZqLGOWYInEGQ6YBmIUHlgPs
    # 通讯录：oKPwlYZ2bMunvnI4q6ZDr94YYZc_a4OxH2KM3oEh82k
