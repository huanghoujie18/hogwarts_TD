# 记录生肖，根据年份来判断生肖

chinese_zodiaz='猴鸡狗猪鼠牛虎兔龙蛇马羊'  # 为什么是从猴年开始？
# 公元1年是鸡年，字符串下标是开始的，所以要以猴年开始
yesr=2018
print(yesr % 12)
print(chinese_zodiaz[(yesr % 12)])
