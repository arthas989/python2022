# 72-4
def findSmallCount(lst, int):
    count = 0
    for i in lst:
        if int > i:
            count += 1
    print(count)


print("------------- 72-4 -------------")
findSmallCount([1, 2, 3], 2)
findSmallCount([1, 2, 3, 4, 5], 0)

# 72-5


def findSmallerTotal(total_list, int):
    '''
    sum elements of total_list that < int
    '''
    sum_list = 0
    for ele in total_list:
        if ele < int:
            sum_list += ele
        else:
            break
    return sum_list


print("------------- 72-5 -------------")
print(findSmallerTotal([1, 2, 3], 3))
print(findSmallerTotal([1, 2, 3], 1))
print(findSmallerTotal([3, 2, 5, 8, 7], 999))
print(findSmallerTotal([3, 2, 5, 8, 7], 0))

# 72-6


def findAllSmall(total_list, int):
    return [i for i in total_list if i < int]


print("------------- 72-6 -------------")
print(findAllSmall([1, 2, 3], 10))
print(findAllSmall([1, 2, 3], 2))
print(findAllSmall([1, 3, 5, 4, 2], 4))


# 72-7
def summ(total_list):
    sum_list = 0
    for ele in total_list:
        sum_list += ele
    return sum_list


print("------------- 72-7 -------------")
print(summ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(summ([]))
print(summ([-10, -20, -30]))
