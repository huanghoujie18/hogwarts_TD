# 统计三国演义中人物姓名出现的次数
# 从hero.txt读取姓名
# 在三国演义文件中一行行查找，发现一个加1

# 读取hero.txt文件中的英雄
with open('hero.txt',encoding='utf-8') as f:
    data=f.read()
    # 使用|进行分割
    print(data.split('|'))

# 读取武器名称
with open('weapon.txt',encoding='utf-8') as f2:
    n=1
    for line in f2.readlines():
        # 只读取奇数行
        if n % 2 == 1:
            # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。不能删除中间部分的字符。
            print(line.strip('\n'))
        n += 1

# 读取三国演义
with open('三国演义.txt',encoding='utf-8') as f3:
    print(f3.read().replace('\n', '')) # 使用空格替换换行符，因为换行可能会拆散姓名和武器
