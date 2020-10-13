# 加入功能：统计生肖和星座的次数


chinese_zodiaz='猴鸡狗猪鼠牛虎兔龙蛇马羊'
# unicode编码
zodiac_name= [u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
              u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座']
# 每个星座的开始日期，1月20日（包括）是摩羯座结束的日期
zodiac_days=((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),(7,23),(8,23),(9,23),(10,23),(11,23),(12,23))

# 使用字典记录生肖和星座的次数
cz_num={}
for i in chinese_zodiaz:
    # 把每一个生肖的次数全部初始化为0
    cz_num[i]=0
print(cz_num)

z_num={}
for i in zodiac_name:
    # 把每个星座的次数初始化为0
    z_num[i]=0
print(z_num)

# 可以多次输入
while True:
    # 用户输入
    yesr=int(input('请输入一个年份：'))
    int_month=int(input('请输入一个月份：'))
    int_day=int(input('请输入一个日期：'))


    # 使用while实现，循环判断zodiac_day中的元组是否小于输入的数值，每判断一次次数累加1，最后通过累加数做为取出星座名的下标值
    n=0
    while zodiac_days[n]<(int_month,int_day):
        # 如果满足下面的条件，就不会执行循环体，那n的值还是0
        if int_month==12 and int_day>23:
            break
        n += 1
    # 这是在循环体之外的语句
    print('%d 是 %s 年'%(yesr,chinese_zodiaz[(yesr % 12)]))
    print('是 %s' %(zodiac_name[n]))

    # 统计生肖的次数
    cz_num[chinese_zodiaz[yesr % 12]] += 1

    # 统计星座的次数
    z_num[zodiac_name[n]] += 1

    # 打印生肖和星座的统计次数
    for each_key in cz_num.keys():  # keys是取出字典cz_num的key，也就是生肖名称，cz_num[each_key]则是生肖的次数
        print('生肖 %s 有 %d 个' %(each_key,cz_num[each_key]))

    for each_key in z_num.keys():   # keys是取出字典z_num的key，也就是星座名称，z_num[each_key]则是星座的次数
        print('星座 %s 有 %d 个' %(each_key,z_num[each_key]))




