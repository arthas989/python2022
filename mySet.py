# 不能直接寫mySet = {} 會變成dict，但可寫mySet = {1,2,3}
mySet = set({1, "everything", 2, "nothing"})
mySet.difference_update([1, "nothing"])
print(mySet)
mySet.remove(2)
print(mySet)
