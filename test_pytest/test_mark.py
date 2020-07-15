import pytest


class TestMethod():
    @pytest.mark.testa
    def test_a(self):
        print('-----test_a-----')

    @pytest.mark.testb
    def test_b(self):
        print('-----test_b-----')


if __name__ == '__main__':
    pytest.main(['-s','test_mark.py'])
