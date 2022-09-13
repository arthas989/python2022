def greet():
    print("greet!!")

# 執行 hello() 會return 一個function


def hello():
    return greet


# 用一個變數welcome接return的function
welcome = hello()
welcome()
