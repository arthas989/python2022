print("------------- 74-5 -------------")


def swap(line):
    # 依序讀入及輸出字元
    # 判斷字元是大寫或小寫
    for letter in line:
        if letter == letter.upper():
            print(letter.lower(), end="")
        else:
            print(letter.upper(), end="")
    print()


swap("Aloha")  # returns "aLOHA"
swap("Love you.")  # returns "lOVE YOU."


def findMin(lst):
    if lst == []:
        return "undefined"
    min_num = lst[0]
    for i in lst:
        if min_num > i:
            min_num = i
    return min_num


print("------------- 74-6 -------------")
print(findMin([1, 2, 5, 6, 99, 4, 5]))
print("------------- 74-6 -------------")
print(findMin([]))
print("------------- 74-6 -------------")
print(findMin([1, 6, 0, 33, 44, 88, -10]))
