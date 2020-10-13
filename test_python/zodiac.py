# unicode编码
zodiac_name=(u'摩羯座',u'水瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',
             u'巨蟹座',u'狮子座',u'处女座',u'天秤座',u'天蝎座',u'射手座')
# 星座的开始日期、结束日期
zodiac_days=((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),(7,23),(8,23),(9,23),(10,23),(11,23),(12,23))
# 用元组储存不变的数据
# 知识点：元组比较大小
print((1,20)<(2,19))  # 可以看作是120与219比较，返回True
print((1,20)>(2,19))  #

(month,day)=(2,15)
# filter过滤器，过滤zodiac_days中小于等于指定日期的数据
zodiac_day = filter(lambda x:x<=(month,day),zodiac_days)
# 统计个数，做为取出星座名称的下标值
print(zodiac_name[len(list(zodiac_day)) %12])  # 其实不需要与12取模也可以吧
