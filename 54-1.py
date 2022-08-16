# x, y are the parameters
def addition(x, y):
    print(x + y)


# 15, 20, a, b are the arguments
addition(15, 20)
a = 30
b = 25
addition(a, b)

a = 5  # global variable


def f1():
    x = 2  # f1 function's local variable
    y = 3  # f1 function's local variable
    print(x, y, a)


def f2():
    x = 10  # f2 function's local variable
    y = 17  # f2 function's local variable
    print(x, y, a)


f1()
