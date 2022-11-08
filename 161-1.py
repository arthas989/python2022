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

# 第一種方式是people.insert().values(XXXX)
insert_statement = people.insert().values(name="Spencer", count=66)
print(str(insert_statement))
# INSERT INTO people (name, count) VALUES (?, ?)
session.execute(insert_statement)
session.commit()

result = session.execute(select([people]))
for row in result:
    print(row)
