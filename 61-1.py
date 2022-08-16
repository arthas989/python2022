# Lambda input1, input2, ... : operation
result = (lambda x: x ** 2)(5)
print(result)

result = (lambda x, y: (x+y, x-y))(15, 30)
print(result)


for item in map(lambda x: x**2, [15, 10, 5, 0]):
    print(item)

for item in filter(lambda x: x % 2 == 0, [15, 10, 5, 0]):
    print(item)
