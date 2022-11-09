# 163-1.py alembic
from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect

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

inspector = inspect(engine)
print(inspector.get_table_names())
