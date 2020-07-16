import pytest

# 参数化
class TestMethod():
    @pytest.mark.parametrize('name',['xiaoming','jack'])
    def test_a(self,name):
        print('-----test_a-----')
        print(name)

    @pytest.mark.parametrize(('username','password'),[('xiaoming','123456'),('jacky','567890')])
    def test_b(self,username,password):
        print('-----test_b-----')
        print('username: "{}",password:"{}"'.format(username,password))


if __name__ == '__main__':
    pytest.main(['-s','test_para.py'])
