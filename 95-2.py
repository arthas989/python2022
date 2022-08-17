# 95-2.py
# 多重繼承的方法解析順序
class G:
    def do_stuff(self):
        print("do stuff from class G")


class F:
    def do_stuff(self):
        print("do stuff from class F")


class E:
    pass


class D(G):
    pass


class C:
    def do_stuff(self):
        print("do stuff from class C")


class B(E, F):
    pass


class A(B, C, D):
    pass


a = A()
a.do_stuff()
# print(a.mro())
# print(a.__mro__)
print(A.mro())
print(A.__mro__)
