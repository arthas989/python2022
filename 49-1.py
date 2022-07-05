# 原始寫法
counter = 1
for letter in "How are you today?":
    if counter < 10:
        print(counter, letter)
    counter += 1

print("------------------------------")

# enumerate 示範
for counter, char in enumerate("How are you today?", start=1):
    if counter < 10:
        print(counter, char)

print("------------------------------")

for tuple in enumerate("How are you today?"):
    print(tuple)

# zip 示範
x = [1, 2]
y = ['A', 'B', 'C', 'D']
z = ['a', 'b', 'c']
for i in zip(x, y, z):
    print(i)

'''
(1, 'A', 'a')
(2, 'B', 'b')
'''
