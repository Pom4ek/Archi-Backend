from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session
from config import DATABASE_URL
from schemas import *


engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session


def create_db_tables():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_tables()