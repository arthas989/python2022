# 136-6.py
# 產生密碼表
f = open("C:\\Users\\user\\Desktop\\python\\python2022\\password.txt", "w")

# 產生6位數字
for id in range(10000000):
    password = str(id).zfill(6) + '\n'
    f.write(password)

f.close()
