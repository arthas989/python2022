
# 118-1.py
def hello():  # 定義的hello func會儲存於電腦內某個記憶體位址
    print("Hello World")


greet = hello  # greet變數存的是hello的記憶體位址
greet()
print(greet)
print(hello)
