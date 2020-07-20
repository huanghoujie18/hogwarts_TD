# *args参数的使用
# 计算除第一个参数外所有参数之和
def calculate_sum(*args):  # args是一个元组
    return sum(args)   # 使用内建函数’sum’,它使用元组或数列作为参数，返回元组所有元素的和。

def ignore_first_calculate_sum(a,*iargs):  # 第一个参数被常规参数’a’接收，其他参数被’iargs’作为元组接收
    required_sum = calculate_sum(*iargs)
    print("sum is ", required_sum)

def test_sum():
    ignore_first_calculate_sum(1,*(2,3,4,5,6))
    '''
    用到函数’calculate_sum’,’calculate_sum’需要多个位置参数作为元组传给’args’,
    所以在函数’ignore_first_calculate_sum’需要拆元组’iargs’,然后将元素作为位置参数传给’calculate_sum’。
    注意,用’*’拆元组
    '''
