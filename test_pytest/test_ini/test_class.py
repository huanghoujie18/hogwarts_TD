import pytest


class TestMethod():
    @pytest.mark.testa
    def test_a(self):
        print('-----test_a-----')

    def test_b(self):
        print('-----test_b-----')

    def setup(self):
        print('-----setup-----')

    def teardown(self):
        print('-----teardown----')

    def setup_class(self):
        print('-----setup_class-----')

    def teardown_class(self):
        print('-----teardown_class----')

if __name__ == '__main__':
    if __name__ == '__main__':
        pytest.main(['-s','test_class.py'])
