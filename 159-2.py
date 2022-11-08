import sqlite3

# conn = sqlite3.connect(":memory:") # 放在MEMORY裡不會出現任何東西
conn = sqlite3.connect("datafile.db")
cursor = conn.cursor()

cursor.execute("""update people set count = :usercount where name = :username""",{"username":"Bob","usercount":39})

result = cursor.execute("select * from people")
print(result.fetchall())
conn.commit()
conn.close()
