import sqlite3

# conn = sqlite3.connect(":memory:") # 放在MEMORY裡不會出現任何東西
conn = sqlite3.connect("datafile.db")
cursor = conn.cursor()

# SQL中給Dict的寫法
cursor.execute(
    """insert into people (name, count) values (:username, :usercount)""",
    {"username": "XMAN", "usercount": 999},
)

cursor.execute("""Delete from people where name = :username""",{"username":"XMAN"})

result = cursor.execute("select * from people")
print(result.fetchall())
conn.commit()
conn.close()
