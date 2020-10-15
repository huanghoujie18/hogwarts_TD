import re

# 定义一个统计英雄次数的方法，返回英雄在三国演义出现的次数
def find_item(hero):
    with open('三国演义.txt',encoding='utf-8') as f:
        data=f.read().replace('\n','')
        name_num=len(re.findall(hero,data))  # findall("匹配规则", "要匹配的字符串") ,以列表形式返回匹配到的字符串
        print('英雄 %s 出现 %d 次' %(hero,name_num))
    return name_num

hero_dict={}
with open('hero.txt',encoding='utf-8') as f:
    f=f.read().strip('\n')   # 去掉英雄最后的换行
    # print(f)
    names=f.split('|')
    # print(names)
    for line in names:
        # 读取全部姓名
        heros=line.split('|')
        # print(heros)  # ['诸葛亮', '曹操', '刘备', '孙权', '赵云', '关羽', '张飞', '黄总', '马超\n']
        # 逐一取出每个姓名，调用find_item方法，查找出现次数
        for hero in heros:
            hero_num=find_item(hero)
            # 使用字典保存每一个姓名和出现的次数
            hero_dict[hero]=hero_num

