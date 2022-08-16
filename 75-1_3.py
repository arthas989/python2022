# 自己寫list排序演算法
def mySort(lst):
    # 把list元素一個一個拿來比，大的往後排
    order_list = []
    for outer_ele in lst:
        if order_list == []:
            order_list.append(outer_ele)
            # print(order_list)
            continue
            # return
        for index, inner_ele in enumerate(order_list):
            # 要知道index是要插入index跟index+1
            # 外層的一個一個拿來比，大的往後放
            if outer_ele > inner_ele:
                continue
            else:
                order_list.insert(index, outer_ele)
                # print(order_list)
                break
                '''
                沒有break會變dead lock 裡面一直加大orderlist
                外面迴圈會跑不完
                '''
                # return
    return order_list


print("------------- 75-1 -------------")
print(mySort([17, 0, -3, 2, 1, 0.5]))

# 判斷質數，質數是除了1及本身，沒有其他數可以整除


def isPrime(num):
    counter = 0
    for i in range(1, num+1, 1):
        if num % i == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False


print("------------- 75-2 -------------")
print(isPrime(1))
print("------------- 75-2 -------------")
print(isPrime(5))
print("------------- 75-2 -------------")
print(isPrime(91))
print("------------- 75-2 -------------")
print(isPrime(1000000))

# 寫判斷回文演算法，回文=正寫逆寫都一樣


def palindrome(myString):
    if myString == myString[::-1]:
        return True
    else:
        return False


print("------------- 75-3 -------------")
print(palindrome("bearaeb"))
print("------------- 75-3 -------------")
print(palindrome("Whatever revetahW"))
print("------------- 75-3 -------------")
print(palindrome("Aloha, how are you today?"))
