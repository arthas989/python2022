# 原始寫法
# counter = 0
# for letter in "How are you today?":
#     if counter < 10:
#         print(letter)
#     counter += 1

# enumerate 示範
# for counter, char in enumerate("How are you today?"):
#     if counter < 10:
#         print(char)

for tuple in enumerate("Today is a good day!!"):
    print(tuple)

# zip 示範
# x = [1, 2]
# y = ['A', 'B', 'C', 'D']
# z = ['a', 'b', 'c']
# for i in zip(x, y, z):
#     print(i)
