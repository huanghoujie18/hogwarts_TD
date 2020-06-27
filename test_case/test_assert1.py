from common.get_mysql import *

a=0
b=1
def test_assert():
    assert a,'断言失败打印的信息'  # 自定义断言失败打印的信息，用逗号隔开
    # assert not a,'断言失败打印的信息'
    assert b,'断言失败打印的信息'

def test_assert_in():
    c='c'
    d='adacde'
    e='aeewd'
    # assert c in d,'断言失败打印的信息'
    assert c not in e,'断言失败打印的信息'
def test_assert_equl():
    assert a!=b
    # assert a==b
    # 对比数据库数据
    # assert a==get_sql("SELECT dept_no FROM departments WHERE dept_name ='Finance'")
