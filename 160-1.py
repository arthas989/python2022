import sqlite3

conn = sqlite3.connect("datafile.db")
name = input("Please type the name you want to search:")
cursor = conn.cursor()
# 可執行sql injection 的查詢方式
# result = cursor.execute("""select * from people where name = '{}'""".format(name))
# select * from people where name = '1' or '1'='1'
# parameterized queries 方式1 放一個dict
# result = cursor.execute(
#     """select * from people where name = :username""", {"username": name}
# )
# parameterized queries 方式2 放一個tuple
result = cursor.execute("""select * from people where name = ?""", (name,))
print(result.fetchall())
conn.commit()
conn.close()
