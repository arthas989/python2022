def printMany():
    for i in range(1, 101, 1):
        print(i)


print("------------- 71-1 -------------")
printMany()


def printEvery3():
    for i in range(1, 89, 3):
        print(i)


print("------------- 71-2 -------------")
printEvery3()


def position(str):
    for counter, char in enumerate(str):
        if char == char.upper():
            return (char, counter)
            break
    return -1


print("------------- 71-3 -------------")
print(position("abcd"))
print(position("AbcD"))
print(position("abCD"))
