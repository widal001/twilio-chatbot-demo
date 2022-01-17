"""Creates a Base model for the SQLAlchemy classes defined in models/ and
imports commonly used SQLAlchemy data types to avoid having to re-import them
across the other model definitions
"""
# pylint: disable=W0611
from __future__ import annotations  # prevents NameError for typehints
from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import relationship, sessionmaker
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


@as_declarative()
class Base:
    """Uses SQLAlchemy's declarative base to create a base model for the
    SQLAlchemy classes defined in models/ and autogenerates __tablename__
    """

    id: Any
    __name__: str
    # Generate __tablename__ automatically

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
