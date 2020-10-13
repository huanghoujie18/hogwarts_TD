# 输出1到10所有偶数的平方

alist=[]
for i in range(1,11):
    if i % 2 == 0:
        alist.append(i*i)
print(alist)

# 列表推导式
blist=[i*i for i in range(1,11) if i % 2 == 0]
print(blist)

chinese_zodiaz='猴鸡狗猪鼠牛虎兔龙蛇马羊'
cz_num={}
for i in chinese_zodiaz:
    # 把每一个生肖的次数全部初始化为0
    cz_num[i]=0
print(cz_num)

# 字典推导式
adict={i:0 for i in chinese_zodiaz}
print(adict)
