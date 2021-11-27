# pylint: disable=W0611
from __future__ import annotations  # prevents NameError for typehints

from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import (
    create_engine,
    func,
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey,
    ForeignKeyConstraint,
)


Base = declarative_base()
