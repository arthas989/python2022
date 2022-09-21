# 122-2.py
# iterator is a subset of iterable
x = [1, 2, 3]
print(dir(x))
# list is not iterator
# 只有__iter__()，沒有__next__()

list_iterator = iter(x)
print(dir(iter(x)))
# __iter__() returns a iterator
# 有__iter__()，也有__next__()
print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))
