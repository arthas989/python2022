# 九九乘法表
for i in (2, 3, 4, 5, 6, 7, 8, 9):
    for j in (1, 2, 3, 4, 5, 6, 7, 8, 9):
        print(f"{i} * {j} = ", i*j)

# 直角三角型怎麼做? 1 12 123 1234 12345
for i in range(1, 6):
    list = [j for j in range(1, 6) if j <= i]
    print(list)

'''
1
12
123
1234
12345
'''

for i in range(1, 6):         # i總共會執行1~5
    for j in range(1, i+1):   # j每次會執行1~i
        print(j, end="")      # 印出j而且不換行
    print()                   # 結束時換行

print("------")
# 倒直角三角
for i in range(1, 6):         # i總共會執行1~5
    for j in range(6-i, 0, -1):   # j每次會執行1~i
        print(j, end="")      # 印出j而且不換行
    print()                   # 結束時換行
