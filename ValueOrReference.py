
import copy
'''
情境：a是巢狀list，第一個元素塞list b [1,2]
以及有第二個num元素value：3 第三個num元素value：999

第一段是說明c直接assign a的list
c與a的 ram address(id)相同
c與a裡頭的元素ram address(id)皆相同是 by reference
c若異動了裡頭的元素，a也會受影響
'''
print("---------------block01------------------")
b = [1, 2]
a = [b, 3, 999]
c = a
print("c_value ", c)  # [[1, 2], 3, 999]
print("a_id ", id(a))  # 1660300611712
print("c_id ", id(c))  # 1660300611712
print("a[0]_id", id(a[0]))  # 1660301221440
print("c[0]_id", id(c[0]))  # 1660301221440
print("a[2]_value ", a[2])  # 999
print("c[2]_value ", c[2])  # 999
print("a[2]_id", id(a[2]))  # 1660298488208
print("c[2]_id", id(c[2]))  # 1660298488208
c[0][0] = 2
c[2] = 8888
print("a_value ", a)  # [[2, 2], 3, 8888]
# 分隔線
print("---------------block02------------------")
'''
第二段是說明 d用shallow copy一個a的list
d與a的 ram address(id)不同
d與a裡頭的元素ram address(id)皆相同是 by reference
d若異動了裡頭的元素，a也會受影響
'''
d = copy.copy(a)
print("d_value ", d)  # [[2, 2], 3, 8888]
print("a_id ", id(a))  # 1660300611712
print("d_id ", id(d))  # 1660301221248
print("a[0]_id", id(a[0]))  # 1660301221440
print("d[0]_id", id(d[0]))  # 1660301221440
print("a[2]_value ", a[2])  # 8888
print("d[2]_value ", d[2])  # 8888
print("a[2]_id", id(a[2]))  # 1660298488208
print("d[2]_id", id(d[2]))  # 1660298488208
d[0][0] = 5
print("a_value ", a)  # [[5, 2], 3, 8888]

# 分隔線
print("---------------block03------------------")
'''
第三段是說明 e用deep copy一個a的list
e與a的 ram address(id)不同
e與a裡頭的元素ram address(id) list元素id不同，num元素id相同
by sharing?
e若異動了裡頭是不同id的list元素，a不受影響，
但我不懂的是為何異動相同id的num元素，
a還是不受影響
又或者說，為何e與a裡頭的元素ram address(id)，num元素為何id相同?
因為id指的是裡頭value的ram address，e與a的相同值的num元素，id就會相同?
'''
e = copy.deepcopy(a)
print("e_value ", e)
print("a_id ", id(a))  # 1660300611712
print("e_id ", id(e))  # 1660301220352
print("a[0]_id", id(a[0]))  # 1660301221440
print("e[0]_id", id(e[0]))  # 1660301220992
print("a[2]_value ", a[2])  # 4
print("e[2]_value ", e[2])  # 4
print("a[2]_id", id(a[2]))  # 1660298488208
print("e[2]_id", id(e[2]))  # 1660298488208
# 異動e裡頭的list元素
e[0][0] = 10
# 異動e裡頭的number元素
e[2] = 10
print("a_value ", a)  # [[5, 2], 3, 8888]
print("e_value ", e)  # [[5, 2], 3, 8888]
print("a[2]_value_id", id(8888))
print("e[2]_value_id", id(10))
print("a[2]_id", id(a[2]))  # 1660298488208
print("e[2]_id", id(e[2]))  # 1660298488208
