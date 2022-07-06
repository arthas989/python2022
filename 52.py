'''
argv要在terminal powershell測試
是執行python程式碼接收參數的列表
例如 python 52.py whatever myFile.txt
就會回傳一個list內容為 ['52.py', 'whatever', 'myFile.txt']
'''
from sys import argv
# print(argv)
if len(argv) < 2:
    pass
   # 判斷是不是有輸入要判斷的檔案名稱
else:
   # pass
   # 開啟argv[1]開始判斷內容
    file = open(argv[1])
    lines = file.read()
    # print(lines)
    # lines是很長的string，目標是一行一行分析，所以用斷行符號分割
    lines = lines.split("\n")
    print(lines)  # a list of string

    word_count = 0
    letter_count = 0

    for line in lines:
        # 在每一行裡再用空白去拆分每個字
        # 判斷如果不是空白行再開始拆分
        if line != "":
            words = line.split(" ")
            word_count += len(words)  # 計算每一行有多少個「字」
            letter_count += len(line)  # 計算每一行多少個「字元」

    line_count = len(lines) - 1
    '''
    為什麼 line_count = len(lines) - 1?
    wilson老師在52節問與答有提到
    Linux系統當中的wc command在計算行數的方式跟我們認知的有些許不同。
    某些計算行數的演算法會把所有文件後方的空白列全部不放入計算，
    有些會全部用1來計，有些會全部計算(像是我課程中演示的方法)。
    此行是指固定扣掉文件中的最後一行空白
    若文件中本來就沒有另一行空白就不用扣
    '''

    # 假設我是出版社的慣老闆，空白行也要全部排除不計
    # 我們由print(lines)中知道空白行也會被分割成一個 '' list的元素
    # 所以只要排除'' 就能排除空白行
    # line_count_list = [l for l in lines if l != '']
    # line_count = len(line_count_list)
    # print(line_count_list)

    print(f"The line count is {line_count}")
    print(f"The word count is {word_count}")
    print(f"The letter count is {letter_count}")
