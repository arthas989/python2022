# 120-2.py
# yeild from的用法

def sub_generator(x):
    for i in range(x):
        yield i ** 2


def gen(y):
    yield from sub_generator(y)


for num in gen(3):
    print(num)

# 0
# 1
# 4
