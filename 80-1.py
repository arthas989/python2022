file = open("myFile3.txt")
print("------------- type(file.readlines()) -------------")
print(type(file.readlines()))  # <class 'list'>
file.seek(0)  # 讀過檔要回到最前面，否則再讀會沒東西

print("------------- type(file.readline()) --------------")
print(type(file.readline()))  # <class 'str'>
file.seek(0)

print("------------- file.readlines() -------------")
print(file.readlines())  # ['line1\n', 'line2']
file.seek(0)
for line_list_ele in file.readlines():
    print(line_list_ele, end='')  # print()設定不換行呈現txt的原始樣貌
print()
file.seek(0)

print("------------- file.readline() -------------")
while True:
    line = file.readline()
    if not line:  # line == ""
        break
    else:
        print(line, end='')

file.close()
