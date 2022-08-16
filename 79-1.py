file = open("myFile3.txt")
print(type(file.read()))  # <class 'str'>
file.seek(0)
print(file.read())
file.seek(0)
print(file.read(5))
