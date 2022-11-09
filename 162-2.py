# 162-2.py 用Object的方式操作資料 UPDATE、DELETE
from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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

Base = declarative_base()


class People(Base):
    __tablename__ = "people"
    # 為什麼id的寫法與其他欄位寫法不同?
    # 判斷id是自動產生，不需要在此指定資料庫對應的欄位
    id = Column(Integer, primary_key=True)
    # id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    count = Column("count", Integer)


Session = sessionmaker(bind=engine)
session = Session()
metadata.create_all(engine)

# create
# new1 = People(name="fakeuser", count=105)
# session.add(new1)

# update
wilson = session.query(People).filter_by(name="wilson").first()
wilson.count = 99
session.add(wilson)
session.commit()

# delete
fakeuser = session.query(People).filter_by(name="fakeuser").first()
session.delete(fakeuser)
session.commit()

# 篩選特定的人
for r in session.query(People).all():
    print(r.id, r.name, r.count)
