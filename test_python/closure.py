# 闭包
# 外部函数的参数被内部函数引用，内部函数对外部参数的参数进行处理，返回一个结果，外部函数返回内部函数（引用内部函数）
def a_func(n):
    def b_func(m):
       return n*m
    return b_func # 注意是没有()，不是b_func()
    # 外函数返回内函数的引用，这里的引用指的是内函数b_func在内存中的起始地址

a=a_func(3)
print(a(4))
print(a(10))
