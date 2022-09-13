def hello():
    print("hello 1")


def hello2():
    print("hello 2")


for fun in [hello, hello2]:
    fun()
