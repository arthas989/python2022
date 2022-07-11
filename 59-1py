def sum(*args):
    result = 0
    for i in range(0, len(args)):
        result += args[i]
        print(f"now result is {result}")
    return result


sum(2, 3, 5, 15)
'''
*args 會packing成tuple
用len(args)當index，加總args[i]
'''


def myfunc(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print("{} is now {} years old.".format(kwargs["name"], kwargs["age"]))


myfunc(name="wilson", age=25, address="Hawaii")

'''
*args 與 **kwargs 可以同時使用
'''


def foodfun(*args, **kwargs):
    print("{} will eat {} {}".format(kwargs["name"], args[0], kwargs["food"]))


foodfun(2, 3, 4, name="wilson", food="eggs")

'''
示範argument的套用順序，若有normal的會先套入
如果少了argument會帶default值

1. normal argument (p1,p2)
2. default argument
3. *args
4. **kwargs
'''


def MixArgument(p1, p2, p3="three", *args, **kwargs):
    print("---------------------------")
    print(p1, p2, p3, args, kwargs)


MixArgument(1, 2, 3, 4, 5, x=1, y=3)
MixArgument(1, 2, 3, 4, x=4)
MixArgument(1, 2, 3, 4)
MixArgument(1, 2, 3)
MixArgument(1, 2)
