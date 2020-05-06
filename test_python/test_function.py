from test_python.function_code import myfunction, namefunction, add


def test_function():
    myfunction()

def test_namefunction():
    namefunction('小甲鱼')

def test_add():
    add(4,5)

# 关键字参数
def saySomething(name,word):
    print(name + '->' + word)

saySomething('小甲鱼','让程序改变世界')
