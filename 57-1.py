def exponent(a, b):
    return a**b


# positional arguments 順序不能錯亂
print(exponent(2, 3))
print(exponent(3, 2))

# keyword arguments 把parameter都寫出來
print(exponent(b=2, a=10))

# 以前用過的地方
# myList is positional argument
# reverse= False is keyword argument
myList = [4, 6, 3, 2, 1]
print(sorted(myList, reverse=False))
