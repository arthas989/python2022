def changeValue(myNum):
    '''
    在def中帶入a
    即myNum = a 
    因為a是num 所以是copy by value
    '''
    num = 10


a = 5
changeValue(a)
print(a)  # a 還是 5


def changeReference(myList):
    '''
    在def中帶入aList
    myList = aList
    list是copy by reference
    '''
    myList[0] = 100


aList = [2, 3, 4, 5]
changeReference(aList)
print(aList)
