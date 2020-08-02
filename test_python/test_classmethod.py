from test_python.classmethod import A


class TestClassmethod:
    def test_func1(self):
        func1 = A()
        func1.func1()
        # A.func1() 这样调用是会报错：因为func1()调用时需要默认传递实例化类后的地址id参数，如果不实例化类是无法调用的

    def test_func2(self):
        A.func2() # 类方法可以直接调用

