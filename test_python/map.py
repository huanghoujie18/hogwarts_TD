# map函数第一个参数是函数，第二个参数是序列（可以是一个序列或多个序列），序列中的每个一参数逐一调用第一个参数，返回一个可迭代的序列

a_list=list(map(lambda x:x*x,[1,2,3,4]))
print(a_list)

b_list=list(map(lambda x,y:x+y,[1,2,3,4],[9,8,7,6]))
print(b_list)
