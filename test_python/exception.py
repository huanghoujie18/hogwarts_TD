try:
    f = open('我为什么是一个文档.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错啦\n错误原因是：' + str(reason))
print('----------------------------------------------------------------')
try:
    sum = 1 + '2'
    f = open('我为什么是一个文档.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错啦\n错误原因是：' + str(reason))
except TypeError as reason:
    print('类型出错啦\n错误原因是：' + str(reason))
# try语句检测范围内一旦出现异常，剩下的语句将不会被执行。所以运行后会只看到“类型出错啦”的异常

print('-----------------------------try-except-finally异常处理-------------------------------------')
try:
    f = open('test.yml')
    print(f.read())
    sum = 1 + '2'
except:
    print('出错了')
finally:
    f.close()

print('-----------------------------配合else使用-------------------------------------')
try:
    int(9)
except:
    print('出错了')
else:
    print('正常')

print('-----------------------------with语句-------------------------------------')
try:
    with open('test1.yml','w') as f:
        print(f.read())
except:
    print('出错了')
