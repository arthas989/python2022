# 139-7.py
import pyzipper

try:
    zip_file = pyzipper.AESZipFile(
        "C:\\Users\\user\\Desktop\\python\\python2022\\new_test.zip", "r")
except:
    print("zipfile not exist")

try:
    password_file = open(
        "C:\\Users\\user\\Desktop\\python\\python2022\\password.txt")
except:
    print("password file not exist")

for line in password_file.readlines():
    # 去除換行符號
    passwd = line.rstrip('\n')
    # 解壓縮zip加密文件
    try:
        zip_file.extractall(pwd=str.encode(passwd))
        print("unzip success,password is:" + passwd)
        break
    except:
        pass
zip_file.close()
password_file.close()
