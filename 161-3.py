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

# 更新
session.execute(people.update().values(count=105).where(people.c.name == "wilson"))

# 查詢
result = session.execute(select([people]).where(people.c.name == "wilson"))

for row in result:
    print(row)
