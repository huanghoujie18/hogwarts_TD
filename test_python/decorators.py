# 装饰器
import time

# 定义装饰函数
# 统计执行时间
def timer(func):
    def wrapper():
        start_time=time.time()
        func()
        stop_time=time.time()
        print('运行的时间 %s' %(stop_time-start_time))
    return wrapper
#
# # 定义被装饰函数
@timer
def i_can_sleep():
    time.sleep(3)

# 调用i_can-sleep方法
i_can_sleep()

# 执行顺序，首先将i_can_sleep()传给timer，也就是timer(i_can_sleep());
# 然后执行wrapper()函数

# 装饰器与闭包的不同点，装饰函数传入的参数是一个函数，闭包传入的参数是一个变量

print('----------------------------------------------被装饰参数带参数------------------------------------------------')

# 被装饰参数带参数，也就是装饰参数的外部函数带参数
# 发现需要先定义装饰函数
def tips(func):
    def nei(a,b):  # 装饰函数内部函数需要接收被装饰函数的参数
        print('start')
        func(a,b)
        print('end')
    return nei

@tips
def sum(a,b):
    print(a+b)

a=sum(8,9)


print('----------------------------------------------装饰器带参数------------------------------------------------')
# 装饰器带参数
def new_tips(args):
    def tips(func):
        def nei(a,b):  # 装饰函数内部函数需要接收被装饰函数的参数
            print('start to %s' % args)
            func(a,b)
            print('end to %s' % args)
        return nei
    return tips

@new_tips('add_module')
def sum(a,b):
    print(a+b)

a=sum(8,9)

@new_tips('sub_module')
def sub(a,b):
    print(a-b)

b=sub(102,98)

print('--------------------------------------------获取被装饰函数的一些信息--------------------------------------------------')
# 还可以获取被装饰函数的一些信息
def new_tips(args):
    def tips(func):
        def nei(a,b):  # 装饰函数内部函数需要接收被装饰函数的参数
            print('func %s start to %s' % (func.__name__,args))
            func(a,b)
            print('func %s end to %s' % (func.__name__,args))
        return nei
    return tips

@new_tips('add_module')
def sum(a,b):
    print(a+b)

a=sum(8,9)

@new_tips('sub_module')
def sub(a,b):
    print(a-b)

b=sub(10,7)
