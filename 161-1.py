from sqlalchemy import create_engine, select, MetaData, table, column, Integer, String
from sqlalchemy.orm import sessionmaker

dbPath = 'datafile.db'
engine = create_engine('sqlite:///%s' % dbPath)
metadata = MetaData(engine)
people = Table('people',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('count', Integer),
)

Session = sessionmaker(bind=engine)
Session = Session()
metadata.create_all(engine)

insert_statement = people.insert().values(name='Spencer', count=66)
print(str(insert_statement))
