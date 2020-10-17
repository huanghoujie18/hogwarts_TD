# zip以最短的可迭代对象，将迭代对象中的参数一个个打包组成元组，然后返回这些元组组成的对象
a = [1,2,3]
b = [4,5,6]
c = [40,50,60,70,80]

a_zap=zip(a,b)
print(list(a_zap))

c_zip=zip(c,b)
print(list(c_zip))

b_zip=zip(a,c)
print(list(b_zip))

a_list,b_list=zip(*zip(a,b))
print(a_list)
print(b_list)
