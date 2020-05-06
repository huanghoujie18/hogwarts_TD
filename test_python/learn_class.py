class A:
    def printf1(self):
        print("A")
class B:
    def printf2(self):
        print("B")
class C(A,B):
    def printf3(self):
        print("C")
        print(A.printf1(self))
        print(B.printf2(self))
bb = C()
bb.printf3()
# 为什么会打印None
