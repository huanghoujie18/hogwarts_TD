# unicode编码
zodiac_name=(u'摩羯座',u'水瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',
             u'巨蟹座',u'狮子座',u'处女座',u'天秤座',u'天蝎座',u'射手座')
# 每个星座的开始日期，1月20日（包括）是摩羯座结束的日期
zodiac_days=((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),(7,23),(8,23),(9,23),(10,23),(11,23),(12,23))
# 用元组储存不变的数据
# 知识点：元组比较大小
print((1,20)<(2,19))  # 可以看作是120与219比较，返回True
print((1,20)>(2,19))  #

# 用户输入月份和日期
int_month=int(input('请输入一个月份：'))
int_day=int(input('请输入一个日期：'))

# 输入的日期和每个星座结束的日期对比
# for zd_num in range(len(zodiac_days)):
#     if zodiac_days[zd_num] >= (int_month,int_day):
#         print(zodiac_name[zd_num])
#         break  # 就跳出循环对比了，不然会把后面的都打印出来
#     # zodiac_day中最大只有(12,23)，输入数值会有大于这个数值的，大于的其实就是摩羯座
#     elif int_month==12 and int_day>23:
#         print(zodiac_name[0])
#         break


# 使用while实现，循环判断zodiac_day中的元组是否小于输入的数值，每判断一次次数累加1，最后通过累加数做为取出星座名的下标值
n=0
while zodiac_days[n]<(int_month,int_day):
    # 如果满足下面的条件，就不会执行循环体，那n的值还是0
    if int_month==12 and int_day>23:
        break
    n += 1
# 这是在循环体之外的语句
print(zodiac_name[n])

