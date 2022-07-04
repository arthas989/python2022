# # for variable in iterable object:
# #     do something here

# # string在for迴圈的示範
# for letter in "Hello World":
#     if letter == letter.upper():
#         print(letter)

# # tuple在for迴圈的示範
# for tuple in [(1, 3), (2, 4), (5, 6)]:
#     print(tuple[0] + tuple[1])

# for a, b in [(1, 3), (2, 4), (5, 6)]: #利用tubple的upacking
#     print(a + b)

# # dictionary在for迴圈的示範
# myDictionary = {"Name": "Kevin", "age": 18}
# for key in myDictionary:
#     print(key)

# for value in myDictionary.values():
#     print(value)

# for key, value in myDictionary.items(): # (key, value) tuple pair.
#     print(f"The key is {key}")
#     print(f"The value is {value}")

# # set在for迴圈的示範
# for i in {3, 1, 5, 9, 7, 1, 3, 5, 7, 9}:
#     print(i)

# packing = 1, 3, 5, 7, 9
# print(type(packing))  # tuple
# for i in packing:
#     print(i)

# for i in 1:
#     print(i) # TypeError: 'int' object is not iterable
