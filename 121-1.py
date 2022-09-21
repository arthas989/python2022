# 121-1.py
# iterable => (1) __iter__()method returns an iterator
# any generator is an iterator
class Something:
    def __iter__(self):
        yield 5
        for x in range(1, 4):
            yield x


s = Something()
# s is an iterable
# iter(iterable) returns an iterator
print(iter(s))
for i in s:
    print(i)

"""
<generator object Something.__iter__ at 0x0000026FCA89A3B0>
5
1
2
3
"""
# 121-1.py
# iterable => (2) implements __getitem__()


class Building(object):
    def __init__(self, floors):
        self.__floors = [None] * floors
        # 做一個 list 用來設定有幾個 None
        # 假設 floors = 3 會得到 [None,None,None]

    # setitem 與 getitem是一組的 用idex來設定值(dict的方式)
    def __setitem__(self, floor_number, data):
        self.__floors[floor_number] = data

    def __getitem__(self, floor_number):
        return self.__floors[floor_number]


building1 = Building(4)
print(building1)
building1[0] = "Reception"
building1[1] = "ABC Corp"
building1[2] = "DEF Inc"

for thing in building1:
    print(thing)
"""
<__main__.Building object at 0x0000026FCA8BFD60>
Reception
ABC Corp
DEF Inc
None
"""
print(building1[1])
# ABC Corp
