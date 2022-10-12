import sys
import os


# 範例程式用的自製路徑檔名
filepath = "whatever\\some\\directory\\path.jpg"

fp = os.path.join(os.getcwd(), "124\\path.jpg")
# print(fp)

# print(os.path.split(filepath)) # ('whatever\\some\\directory', 'path.jpg')
# print(os.path.split(fp)) # ('c:\\Users\\user\\Desktop\\python\\python2022\\124', 'path.jpg')

# print(os.path.basename(filepath)) # path.jpg
# print(os.path.basename(fp))  # path.jpg

# print(os.path.dirname(filepath))  # whatever\some\directory
# print(os.path.dirname(fp))  # c:\Users\user\Desktop\python\python2022\124

# print(os.path.splitext(filepath))
# ('whatever\\some\\directory\\path', '.jpg')

# print(os.path.abspath("124-1.py"))

# OS Constants
# print(os.name)  # nt
# print(sys.platform)  # win32

print(os.path.isfile("c:\\Users\\user\\Desktop\\python\\python2022\\124-1.py"))  # True
print(os.path.isdir("c:\\Users\\user\\Desktop\\python\\python2022\\124-1.py"))  # False
print(os.path.exists("c:\\Users\\user\\Desktop\\python\\python2022\\124-1.py"))  # True
