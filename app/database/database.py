from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL
from app.database.schemas import *


engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    Session = sessionmaker(engine)
    with Session() as session:
        return session
    

def create_db_tables():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_tables()