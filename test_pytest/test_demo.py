import pytest

def func(x):
    return x+1

def test_b():
    print('-----test_b-----')
    assert func(3)==5  # 断言失败

def test_a():
    print('-----test_a-----')
    assert func(3)==4   # 断言成功



if __name__=="__main__":
    pytest.main(['-s','test_demo.py'])
    # 使用命令行执行：pytest -s test_demo.py

