import sqlite3

# conn = sqlite3.connect(":memory:") # 放在MEMORY裡不會出現任何東西
conn = sqlite3.connect("datafile.db")
cursor = conn.cursor()
cursor.execute(
    """create table people (id integer primary key, name text, count integer)"""
)
# 直接寫在SQL中
cursor.execute("""insert into people (name, count) values ('Bob', 15)""")
# SQL中給問號，後面帶tuple的寫法
cursor.execute("""insert into people (name, count) values (?, ?)""", ("Kevin", 20))
# SQL中給Dict的寫法
cursor.execute(
    """insert into people (name, count) values (:username, :usercount)""",
    {"username": "Grace", "usercount": 27},
)

conn.commit()
conn.close()
