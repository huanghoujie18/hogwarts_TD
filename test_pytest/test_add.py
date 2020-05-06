
from test_pytest.add import add

def test_add_int():
    print('\n测试test_add_int()')
    assert add(3, 4) == 7

def test_add_float():
    print('\n测试test_add_float()')
    assert add(3.5, 7.0) == 10.5
