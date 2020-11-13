import os
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Integer
from sqlalchemy import Sequence
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import postgresql
from dotenv import load_dotenv


load_dotenv()


base = declarative_base()
SOLUTIONS_ID = Sequence("solutions_id_seq")


class Solution(base):
    __tablename__ = "solutions"

    id = Column(
        Integer,
        SOLUTIONS_ID,
        primary_key=True,
        server_default=SOLUTIONS_ID.next_value(),
    )
    queens = Column(Integer, nullable=False, index=True)
    bt_solution = Column(postgresql.ARRAY(Integer), nullable=False)

    def __init__(self, queens, bt_solution):
        self.queens = queens
        self.bt_solution = bt_solution


class DBhandler:
    db = os.getenv("POSTGRES_DB")
    port = os.getenv("POSTGRES_PORT")
    host = os.getenv("POSTGRES_HOST")
    username = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    db_string = f"postgresql://{username}:{password}@{host}:{port}/{db}"

    def __init__(self):
        self.db = create_engine(self.db_string)
        Session = sessionmaker(self.db)
        self.session = Session(bind=self.db, autoflush=False)

        base.metadata.create_all(self.db)

    def get_solutions(self, queens):
        return self.session.query(Solution).filter(Solution.queens == queens).all()

    def bulk_save_objects(self, objects):
        self.session.bulk_save_objects(objects)

    def add(self, row):
        self.session.add(row)

    def commit(self):
        self.session.commit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()
