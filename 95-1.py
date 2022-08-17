# 95-1.py
# 最簡單的multiple inheritance
class C:
    def stuff_c(self):  # 養成習慣記得放self
        print("do stuff from class c")


class D:
    def stuff_d(self):
        print("do stuff from class d")


class A(C, D):
    pass


a = A()
a.stuff_c()
a.stuff_d()
