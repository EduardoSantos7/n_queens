from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import postgresql


base = declarative_base()


class Solution(base):
    __tablename__ = 'solutions'

    queens = Column(Integer, primary_key=True)
    bt_solution = Column(postgresql.ARRAY(Integer, dimensions=2))


class DBhandler:
    db_string = "postgresql://reysantos7:05120714@localhost:5437/test"

    def __init__(self):
        self.db = create_engine(self.db_string)
        Session = sessionmaker(self.db)
        self.session = Session()

        base.metadata.create_all(self.db)

    def add(self, row):
        self.session.add(row)

    def commit(self):
        self.session.commit()
