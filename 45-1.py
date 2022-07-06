'''
重要 要理解或背起來 巢狀迴圈的運作規則
The "inner loop" will be executed one time for 
each iteration of the "outer loop".
'''
counter = 0
for i in "1234":
    for j in "abcd":
        print(i, j)
        counter += 1
print(f"counter is now {counter}")
# 總共執行次數 i x j = 16
'''
i = 1, j=a  =>  1,a
       j=b  =>  1,b
       j=c  =>  1,c
       j=d  =>  1,d
i = 2, j=a  =>  2,a
       j=b  =>  2,b ......
'''

print("------")

# 九九乘法表
for i in (2, 3, 4, 5, 6, 7, 8, 9):
    for j in (1, 2, 3, 4, 5, 6, 7, 8, 9):
        print(f"{i} * {j} = ", i*j)

# 直角三角型怎麼做? 1 12 123 1234 12345
for i in range(1, 6):
    list = [j for j in range(1, 6) if j <= i]
    print(list)

'''
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
'''

for i in range(1, 6):         # i總共會執行1~5
    for j in range(1, i+1):   # j每次會執行1~i
        print(j, end="")      # 印出j而且不換行
    print()                   # 結束時換行

'''
1
12
123
1234
12345
'''

print("------")


# 倒直角三角
for i in range(1, 6):         # i總共會執行1~5
    for j in range(6-i, 0, -1):   # j每次會執行1~i
        print(j, end="")      # 印出j而且不換行
    print()                   # 結束時換行

'''
54321
4321
321
21
1
'''
