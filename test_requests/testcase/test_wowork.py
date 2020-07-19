from test_requests.api.wework1 import WeWork


class TestWeWork():
    def test_get_token(self):
        secret = 'oKPwlYZ2bMunvnI4q6ZDr94YYZc_a4OxH2KM3oEh82k'
        r=WeWork.get_token(secret)
        print(r)
