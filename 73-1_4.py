def stars(num):
    if num >= 1:
        for i in range(1, num+1):
            print(i*"*")
    else:
        return


print("------------- 73-1 -------------")
stars(1)
print("------------- 73-1 -------------")
stars(4)


def stars2(num):
    if num >= 1:
        for i in range(1, num+1, 1):  # 往上加時沒忘記要加1
            print(i*"*")
        for i in range(num-1, 0, -1):  # 往下減時就忘了要設到0
            print(i*"*")
    else:
        return


print("------------- 73-2 -------------")
stars2(1)
print("------------- 73-2 -------------")
stars2(2)
print("------------- 73-2 -------------")
stars2(3)
print("------------- 73-2 -------------")
stars2(4)


def table(num):
    if num >= 1:
        for j in range(1, 10, 1):
            print(f"{num} x {j} = ", num*j)
    else:
        return


print("------------- 73-3 -------------")
table(3)


def table9to9():
    for i in range(1, 10, 1):
        for j in range(1, 10, 1):
            print(f"{i} x {j} = ", i*j)


print("------------- 73-4 -------------")
table9to9()
