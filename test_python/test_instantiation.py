# 类的实例化instantiation
class Tea:
    def __init__(self):
        print('Dahongpao Tea')
# 类不带括号我们叫赋值，带括号我们叫实例化。
def test_tea():
    b = Tea()
    print(id(Tea))
    print(id(b))
    print(Tea)
    print(b)

