# A = [1, 3, 4, 5, 6, 7, 9]
# # 用loop印出A list中每個數的平方「的list」
# # 傳統方法
# L = []
# for i in A:
#     L.append(i**2)
# print(L)

# 用列表推導式 [expr for var in iterable]
# B = [x**2 for x in A]
# print(B)  # [1, 9, 16, 25, 36, 49, 81]

# # 用loop印出A list中 奇數 的平方
# C = [y**2 for y in A if y % 2 == 1]
# print(C)  # [1, 9, 25, 49, 81]

# '''
# list中最前面的變數是我們要操作或要保留的
# 這段拆分為if xxx else yyy statement，以及後面的for迴圈
# 如果xxx是奇數就+1，若yyy就保留不做動作
# A = [1, 3, 4, 5, 6, 7, 9]
# '''
# D = [z+1 if z % 2 == 1 else z for z in A]
# print(D)

# # dict comprehension
x = [1, 2, 3, 4]
x_squared_dict = {item: item**2 for item in x if item > 2}
print(x_squared_dict)  # {3: 9, 4: 16}

# # set comprehension
x_squared_set = {item**2 for item in x if item > 2}
print(x_squared_set)  # {16, 9}

# # generator comprehension
x_squared_generator = (item ** 2 for item in x)
print(x_squared_generator)
# <generator object <genexpr> at 0x000001FEB51DCAC0>
for x in x_squared_generator:
    print(x)
