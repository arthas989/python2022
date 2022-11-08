import sqlite3

# conn = sqlite3.connect(":memory:") # 放在MEMORY裡不會出現任何東西
conn = sqlite3.connect("datafile.db")
cursor = conn.cursor()

result = cursor.execute("select * from people")
print(result.fetchmany(2))

result = cursor.execute("select * from people where name=:username",{"username":"Grace"})
print(result.fetchall())

conn.commit()
conn.close()
