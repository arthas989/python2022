def higherOrder(func):
    func()


def smallFunc():
    print("Hello World!!")


higherOrder(smallFunc)  # 把function的名稱當作argument傳入

print("-------------------")

# map()


def square(num):
    return num ** 2


myList = [-5, 3, 6]
print(map(square, myList))  # map object
for item in map(square, myList):
    print(item)

print("-------------------")

# filter()


def even(num):
    return num % 2 == 1


myList2 = [12314, 43157, 32789]
for item in filter(even, myList2):
    print(item)
