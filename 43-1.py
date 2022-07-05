# for variable in iterable object:
#     do something here

# string在for迴圈的示範
for letter in "Hello World":
    if letter == letter.upper():
        print(letter, end="")

print()

# tuple在for迴圈的示範
for tuple in [(1, 3), (2, 4), (5, 6)]:
    print(tuple[0] + tuple[1])
'''
4
6
11
'''
for a, b in [(1, 3), (2, 4), (5, 6)]:  # 利用tubple的upacking
    print(a + b)
'''
4
6
11
'''

# dictionary在for迴圈的示範
myDictionary = {"Name": "Kevin", "age": 18}
for key in myDictionary:
    print(key)
'''
Name
age
'''
for value in myDictionary.values():
    print(value)
'''
Kevin
18
'''
for key, value in myDictionary.items():  # (key, value) tuple pair.
    print(f"The key is {key}")
    print(f"The value is {value}")
'''
The key is Name
The value is Kevin
The key is age
The value is 18
'''

# set在for迴圈的示範
for i in {3, 1, 5, 9, 7, 1, 3, 5, 7, 9}:
    print(i, end="")
print()

packing = 1, 3, 5, 7, 9
print(type(packing))  # <class 'tuple'>
for i in packing:
    print(i, end="")
print()

# for i in 1:
#     print(i) # TypeError: 'int' object is not iterable
