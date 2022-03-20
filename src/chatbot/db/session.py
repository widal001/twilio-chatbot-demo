"""Used by the get_db() dependency function to create and yield a SQLAlchemy
session object that organizes and executes transactions against the datbase
"""
from typing import Generator

from dynaconf import Dynaconf
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from chatbot import config


def get_db(settings: Dynaconf = config.settings) -> Generator:
    """Dependency injection function that creates and yields a connection
    to the database for to manage db transactions
    """
    engine = create_engine(settings.database_url, pool_pre_ping=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
