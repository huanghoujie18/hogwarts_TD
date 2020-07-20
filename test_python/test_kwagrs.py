
def fun(a,**kwargs):
    print('a is :',a)
    print("We expect kwargs 'b' and 'c' in this function")
    print("b is ", kwargs['b'])
    print("c is ", kwargs['c'])

def test_kwargs():
    fun(1,b=3,c=44)
    '''
    fun(1, {'b':2, 'c':34}),这样调用会报错：ypeError: fun() takes exactly 1 argument (2 given)
    尽管’kwargs’接收键值参数作为一个字典,但你不能传一个字典作为位置参数给’kwargs’
    可以这样调用：fun(1, **{'b':2, 'c':34})
    在一个字典前使用”**”可以unpack字典,传字典中的数据项作为键值参数。
    '''
