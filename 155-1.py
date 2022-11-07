import csv
with open("file2.csv", mode="a", newline="", encoding="cp950") as f:
    csv_writer = csv.writer(f, delimiter=",")
    csv_writer.writerow(['a', 'b', 'c'])
    csv_writer.writerows([['d', 'e', 'f'], ['g', 'h', 'i']])  # 外面要有中括號
