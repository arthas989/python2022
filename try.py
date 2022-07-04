# Dictionary
# 假設1個dict裡面有兩對資料，分別為male及female 用大括號{}
# 裡頭再各放1個dict有兩對資料，name及age 用大括號{}
# name及age都是list 用中括號[]
person = {"male": {"name": ["Wilson", "Mike", "Jerry"], "age": [
    25, 35, 45]}, "female": {"name": ["Elsa", "Irren"], "age": [27, 37]}}


# 可以用index找出值嗎? 定義dictionary是unordered key-value pairs
# 所以直接用index找值會出現錯誤
# print(person[0][1][2]) # KeyError: 0

# 在python 3.7 把dictionary轉成list 可以找到key跟value
# key
print(list(person)[0])  # male
print(list(person)[1])  # female

# value 用dictionary.values() 轉成list就能用index
print(list(person.values())[0])  # mail的value
# {'name': ['Wilson', 'Mike', 'Jerry'], 'age': [25, 35, 45]}

# 課程教要找到dictionaty裡面的值，用[key]去找，若後面有list可以帶index找值
print(person["female"]["age"][1])  # 37

# 如何全部用index去找值?? 用上面的方式全部轉換成list
# 假設目標一樣是找到female的第二筆age 37
# 因為要找female裡面的value
# 所以用person.values()轉成list的index[1]
# 就能找到female裡的值
print(list(person.values())[1].values())
# dict_values([['Elsa', 'Irren'], [27, 37]])

# 因為上面這個還是一個dict分別是key為name與age，跟他成對的值
# 要取值一樣要再加上.values()並轉成list就能用index取值
print(list(list(person.values())[1].values())[1])
# [27, 37]

# 最後在list上選擇目標所需的第2筆 37
print(list(list(person.values())[1].values())[1][1])


# items
# print(person.items())
