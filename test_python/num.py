# 分解质因数
num = int(input("请输入一个合数："))
n = num
list1 = []  #存放质因数
for j in range(int(n/2)+1):
    for i in range(2,n):
        if num % i == 0:  #可以整除
            list1.append(i)
            num = num // i
            break
if len(list1) == 0:
    print("此数是是质数，请重新输入另一个数")
    exit()
#print(list1)
print('%d = '%(n),end='')
for i in range(len(list1)):
    if i  == len(list1)-1:
        print('%s' % (list1[i]))
    else:
        print('%s * ' % (list1[i]),end='')
