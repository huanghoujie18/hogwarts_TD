# encoding:utf-8
import sys

class GetText():
    def __init__(self):
        pass

    @staticmethod
    def A():
        print("this is a staticmethod function")

    def B(self):
        print("this is a func")
    c = "cc desc"

    @staticmethod
    def test_getattr():
        print(sys.modules[__name__])  # <module '__main__' from 'D:/脚本项目/lianxi/clazz/test.py'>
        print(GetText)   #  <class '__main__.GetText'>
        # 获取函数
        print(getattr(GetText, "A"))   # <function GetText.A at 0x00000283C2B75798>
        # 获取函数返回值
        getattr(GetText, "A")()    # this is a staticmethod function
        getattr(GetText(), "A")()   # this is a staticmethod function

        print(getattr(GetText, "B"))    # <function GetText.B at 0x000001371BF55798>
        # 非静态方法不可用
        # getattr(GetText, "B")()
        getattr(GetText(), "B")()     # this is a func
        print(getattr(GetText, "c"))  # cc desc
        print(getattr(GetText(), "c"))   # cc desc
