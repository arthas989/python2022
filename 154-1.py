import csv
with open("file.csv", newline="", encoding="cp950") as f:
    csv_data = csv.reader(f)
    # print(csv_data)
    # <_csv.reader object at 0x00000130B1812740> 是一個iterable
    for row in csv_data:
        print(row)
    f.seek(0)  # 開過的檔案再回到最前面用seek 80-1.py
    for row in csv_data:
        print(row[1].title())
