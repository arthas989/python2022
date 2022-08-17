# 92-2.py
class Circles:
    pi = 3.14159
    all_circles = []

    def __init__(self, radius):
        self.radius = radius
        self.__class__.all_circles.append(self)
        # print(type(self))  # <class '__main__.Circles'>
        # print(self)  # instance 的 記憶體位址
        # print(type(Circles))  # <class 'type'>
        # print(Circles)  # <class '__main__.Circles'>

    def area(self):
        # print(type(self)) # <class '__main__.Circles'>
        # print(self) # object 的 記憶體位址
        return self.__class__.pi * (self.radius ** 2)

    @staticmethod
    def total_area():
        total = 0
        for circle in Circles.all_circles:
            total += circle.area()
        # print(type(Circles))  # <class 'type'>
        # print(Circles)  # <class '__main__.Circles'>
        return total

    @classmethod
    def total_area2(cls):
        total = 0
        for circle in cls.all_circles:
            total += circle.area()
        # print(type(cls))  # <class 'type'>
        # print(cls)  # <class '__main__.Circles'>
        return total


c1 = Circles(10)
c2 = Circles(15)
print(c1.__class__.total_area())
print(c1.__class__.total_area2())
# print(c1) # 與第一次印出的sefl instance 的 記憶體位址 相同
# print(c2) # 與第二次印出的sefl instance 的 記憶體位址 相同
# self代表的是class的instance，而非class

# self不必非寫成self


class Test:
    def prt(this):
        print(this)
        print(this.__class__)


t = Test()
t.prt()
# <__main__.Test object at 0x0000022E93B5C5B0>
# <class '__main__.Test'>

# self可以不寫嗎?


class Test2:
    def prt():
        print("no instance")


Test2.prt()  # no instance
