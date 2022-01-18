from typing import Generator

from chatbot.db import session


def get_db() -> Generator:
    """Dependency injection function that creates and yields a connection
    to the database for to manage db transactions
    """
    try:
        db = session.SessionLocal()
        yield db
    finally:
        db.close()
