# 记录生肖，根据年份来判断生肖

chinese_zodiaz='猴鸡狗猪鼠牛虎兔龙蛇马羊'  # 为什么是从猴年开始？
# 公元1年是鸡年，字符串下标是开始的，所以要以猴年开始
# yesr=int(input('请输入一个年份：'))
# print(yesr % 12)
# print(chinese_zodiaz[(yesr % 12)])

# if chinese_zodiaz[yesr % 12] =='狗':
#     print('狗年运势...')


# for x in chinese_zodiaz:
#     print(x)
#
# for x in range(11):
#     print(x)
#
# for yesr in range(2000,2019):
#     print('%d 年的生肖是 %s' % (yesr,chinese_zodiaz[(yesr % 12)]))

#
# num=6
# while True:
#     print('a')
#     num += 1
#     if num > 10:  # 当num大于10跳出循环
#         break

import time
num = 5
while True:
    num += 1
    if num == 10:
        continue
    print(num)
    time.sleep(1)
