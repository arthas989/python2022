# 162-1.py 用Object的方式操作資料 CREADE、READ
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
    # 為什麼id的寫法與其他欄位寫法不同?是因為PK嗎
    id = Column(Integer, primary_key=True)
    # 測試下面這樣也可以
    # id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    count = Column("count", Integer)


Session = sessionmaker(bind=engine)
session = Session()
metadata.create_all(engine)

# new1 = People(name='Jane',count=5)
# new2 = People(name='Jared',count=35)
# new3 = People(name='Keith',count=45)
# new4 = People(name='Mark',count=55)
# session.add(new1)
# session.add(new2)
# session.add(new3)
# session.add(new4)

session.commit()

# 找符合Class的所有人
for r in session.query(People).all():
    # print(r) # 會列出記憶體位址
    print(r.id, r.name, r.count)

# 篩選特定的人
for r in session.query(People).filter_by(name="wilson"):
    print(r.id, r.name, r.count)
