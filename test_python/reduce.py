# reduce函数，第一个参数是函数，第二个参数是序列，
# 函数有两个参数，先取出序列中最前面的两个参数进行函数处理，得到的结果做为一个参数，与序列中下一个参数又进行函数处理
# 直到把序列的全部参数处理完，然后返回函数处理的结果
from functools import reduce

a=reduce(lambda x,y:x+y, [1,2,3,4,5])
print(a)

b=reduce(lambda x,y:x*y,[1,2,3,4,5])
print(b)
