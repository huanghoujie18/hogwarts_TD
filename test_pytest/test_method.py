import pytest


# def test_a():
#     print('-----test_a-----')
#
# def test_b():
#     print('-----test_b-----')
#
# def setup():
#     print('-----setup-----')
#
# def teardown():
#     print('-----teardown----')
#
# if __name__ == '__main__':
#     if __name__ == '__main__':
#         pytest.main(['-s','test_method.py'])

class Test_method():
    def test_a(self):
        print('-----test_a-----')

    def test_b(self):
        print('-----test_b-----')

    def setup(self):
        print('-----setup-----')

    def teardown(self):
        print('-----teardown----')

if __name__ == '__main__':
    if __name__ == '__main__':
        pytest.main(['-s','test_method.py'])
