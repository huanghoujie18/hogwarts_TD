# filter第一个参数是函数，第二个参数是序列，根据函数过滤序列中的每一个参数，返回符合条件的参数，形成一个可迭代的序列
# 过滤出列表中的所有奇数
def is_odd(n):
    return n % 2 == 1

a_list=list(filter(is_odd,[1,2,3,4,5,6,7,8,9]))
print(a_list)

b_list=list(filter(lambda x:x % 2==1,[1,2,3,4,5,6,7,8,9]))
print(b_list)
