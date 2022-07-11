def myAddition(a, b):
    for i in range(a):
        for j in range(b):
            if i == 3 and j == 4:
                return
            print(i, j)


print(myAddition(10, 15))


def myAddition2(x, y):
    return x+y


print(myAddition2(5, 5)+myAddition2(5, 5))
