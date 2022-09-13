# 96-1.py
class E():
    def do_stuff(self):
        print("do stuff from class E")


class F():
    def do_stuff(self):
        print("do stuff from class F")


class A(E, F):
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d = D()
d.do_stuff()  # do stuff from class E
print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.E'>, <class '__main__.F'>, <class 'object'>]
