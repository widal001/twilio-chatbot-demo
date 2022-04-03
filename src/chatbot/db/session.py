"""Used by the get_db() dependency function to create and yield a SQLAlchemy
session object that organizes and executes transactions against the datbase
"""
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from chatbot import config

DB_URL = config.settings.database_url


def get_db(conn_url: str = DB_URL) -> Generator:
    """Dependency injection function that creates and yields a connection
    to the database for to manage db transactions
    """
    engine = create_engine(conn_url, pool_pre_ping=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
