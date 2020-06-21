# Python调用函数带括号和不带括号的区别
def bracket(data):
    return data

def test_bracket():
    # 不带括号调用的结果：是函数所在内存地址。a是整个函数体，是一个函数对象，不须等该函数执行完成
    a = bracket
    print(a)
    # 带括号调用的结果：6 。b是函数执行后返回的值6,须等该函数执行完成的结果
    b = bracket(6)
    print(b)
