def has_33(lst):
    for counter, ele in enumerate(lst):
        if ele == 3 and lst[counter+1] == 3:
            return True
    return False


print("------------- 77-6 -------------")
print(has_33([1, 5, 7, 3, 3]))
print("------------- 77-6 -------------")
print(has_33([]))
print("------------- 77-6 -------------")
print(has_33([4, 3, 2, 1, 0]))


def spyGame(lst):
    counter = 0
    for ele in lst:
        if ele == 0:
            counter += 1
    if counter >= 2 and 7 in lst:
        return True
    else:
        return False


print("------------- 77-7 -------------")
print(spyGame([1, 2, 4, 0, 3, 0, 7]))
print("------------- 77-7 -------------")
print(spyGame([1, 2, 5, 0, 3, 1, 7]))
