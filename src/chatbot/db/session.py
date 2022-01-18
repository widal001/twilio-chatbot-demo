"""Used by the get_db() dependency function to create and yield a SQLAlchemy
session object that organizes and executes transactions against the datbase
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from chatbot import config

engine = create_engine(config.settings.database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
