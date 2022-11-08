from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker

dbPath = "datafile.db"
engine = create_engine("sqlite:///%s" % dbPath)
metadata = MetaData(engine)
people = Table(
    "people",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("count", Integer),
)

Session = sessionmaker(bind=engine)
session = Session()
metadata.create_all(engine)

# 第二種方式是sql statement放people.insert()，後面選項放dict
insert_statement = people.insert()
print(str(insert_statement))
# INSERT INTO people (id, name, count) VALUES (?, ?, ?)
# session.execute(insert_statement)
session.execute(
    insert_statement,
    [
        {"name": "wilson", "count": 35},
        {"name": "Naleo", "count": 40},
    ],
)
session.commit()

result = session.execute(select([people]))
for row in result:
    print(row)
