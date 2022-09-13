# 比較list 及 yield (generator object)用法
# 使用list
def cube(n):  # 這樣的寫法 list長度越長越佔記憶體空間
    result = []
    for x in range(n):
        result.append(x ** 3)
    return result


for i in cube(3):
    print(i)

print("-"*20)

# 使用yield 預設就會return一個generator object


def cube2(n):
    for x in range(n):
        yield x ** 3


print(cube2(3))
for ele in cube2(3):
    print(ele)

print("-"*20)
# yeild from的用法 傳送一個generator到另一個generaotr


def sub_generator(x):
    print("sub_generator(x)")
    print(sub_generator(x))
    for i in range(x):
        yield i ** 2


def gen(y):
    print("gen(y)")
    print(gen(y))
    yield from sub_generator(y)


print("gen(3)")
print(gen(3))
for num in gen(3):
    print(num)
