def myfunction():
    print('这是我的第一个函数')

def namefunction(name):
    print(name + "是帅哥。")

def add(num1,num2):
    return num1 + num2

# 关键字参数
def saySomething(name,word):
    print(name + '->' + word)

saySomething('小甲鱼','让程序改变世界')
saySomething('让程序改变世界','小甲鱼')
saySomething(word='让程序改变世界',name='小甲鱼')

# 默认参数
def saySomething2(name='小甲鱼',words='让程序改变世界'):
    print(name + '->' + words)
saySomething2()
saySomething2('苏轼','不识庐山真面目，只缘身在此山中。')

# 收集参数/可变参数
def test(*params):
    print('有 %d 个参数' % len(params))
    print(params)
test('s','2')
test(*['22','deed','fsa'])

# 可变参数+默认参数
def test1(*params,extra='9'):
    print('可变参数是：',params)
    print('位置参数是：',extra)
test1(1,2,3)
# 传参有些特别
test1(1,34,44,extra=90)

def test2(**params):
    print(params)
test2(Jack=20,Tom=29)
personinfo={'Tony':'20','Neo':30}
test2(**personinfo)
test2(**{'Tony':'20','Neo':30})

# 匿名函数
g = lambda x : 2 * x + 1
print(g(3))

a = lambda x,y : x + y
print(a(6, 9))
