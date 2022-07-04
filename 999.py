a = [[1, 2], [4, 5]]
f = 1
for i in range(2):
    f *= 10
for j in range(2):
    print(i)
    print(a[j][i])
    print(f)
    a[j][i] *= f
print(a)
