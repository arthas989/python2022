import sys
x = 10


def hello():
    x = 10
    print("print hello def's locals")
    print(locals())
    print("print hello def's globals")
    print(globals())


print(type(dir(__builtins__)))
print("----------builtins----------")
print(dir(__builtins__))
print("----------globals----------")
print(globals())
print("----------locals----------")
print(locals())
print("----------def hello----------")
hello()
