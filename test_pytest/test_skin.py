import pytest


class TestMethod():
    @pytest.mark.skip(reason="不要执行的用例")  # reason可以不写
    def test_a(self):
        print('-----test_a-----')

    @pytest.mark.skipif(0>1,reason="不要执行的用例")
    def test_b(self):
        print('-----test_b-----')


if __name__ == '__main__':
    pytest.main(['-s','test_mark.py'])
