# pylint: disable=redefined-builtin
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

import sqlalchemy as sa
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

from chatbot.db.base import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """CRUD class with default methods to Create, Read, Update, Delete (CRUD)

    Parameters
    ----------
    model: Type[ModelType]
        A SQLAlchemy model class for which CRUD operations will be supported
    schema: Type[BaseModel]
        A Pydantic model (schema) class to use to return the
    """

    def __init__(self, model: Type[ModelType]):
        """Inits the CRUD class with a given SQLAlchemy model"""
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        """Uses the primary key to return a single record from the table that
        corresponds to the SQLAlchemy model being queried

        Parameters
        ----------
        db: Session
            Instance of SQLAlchemy session that manages database transactions
        id: Any
            The value of the primary key used to retrieve the record

        Returns
        -------
        Optional[ModelType]
            Returns an instance of the SQLAlchemy model being queried if a row
            is found for the primary key value passed, or None otherwise
        """
        return db.get(self.model, id)

    def get_many(
        self,
        db: Session,
        *,
        skip: int = 0,  # must be passed as keyword argument
        limit: int = 100,  # must be passed as keyword argumet
    ) -> List[ModelType]:
        """Returns a list of records from the table that corresponds to the
        SQLAlchemy model being queried

        Parameters
        ----------
        db: Session
            Instance of SQLAlchemy session that manages database transactions
        skip: int, optional
            The number of rows to skip in the table before returning a row
        limit: int, optional
            The maximum number of rows to return in the query result

        Returns
        -------
        List[ModelType]
            Returns a list of instances of the SQLAlchemy model being queried
        """
        stmt = sa.select(self.model).offset(skip).limit(limit)
        return db.execute(stmt).scalars().all()

    def create(
        self,
        db: Session,
        *,
        data: CreateSchemaType,  # must be passed as keyword argument
    ) -> ModelType:
        """Inserts a new row into the table that corresponds to the SQLAlchemy
        model being created

        Parameters
        ----------
        db: Session
            Instance of SQLAlchemy session that manages database transactions
        data: CreateSchemaType
            The instance of the Pydantic schema that contains the data used to
            insert a new row in the database
        """
        data = jsonable_encoder(data)  # makes data JSON-compatible
        record = self.model(**data)  # type: ignore
        return self.commit_changes(db, record)

    def update(
        self,
        db: Session,
        *,
        record: ModelType,
        update_obj: Union[UpdateSchemaType, Dict[str, Any]],
    ) -> ModelType:
        """Updates the values of the row that corresponds to the SQLAlchemy
        model instance passed as an argument to the record parameter

        Parameters
        ----------
        db: Session
            Instance of SQLAlchemy session that manages database transactions
        record: ModelType
            Instance of the SQLAlchemy model that represents the row in the
            corresponding database table that will be updated
        update_obj: Union[UpdateSchemaType, Dict[str, Any]]
            Either an instance of a Pydantic schema or a dictionary of values
            used to update the row in the database
        """
        # convert record to dict so we can access its fields
        current_data = jsonable_encoder(record)

        # get the update data in dict format
        if isinstance(update_obj, dict):
            update_data = update_obj
        else:
            update_data = update_obj.dict(exclude_unset=True)

        # update the record with the update data
        for field in current_data:
            if field in update_data:
                setattr(record, field, update_data[field])

        return self.commit_changes(db, record)

    def delete(self, db: Session, *, id: Any) -> ModelType:
        """Deletes the row of the table that matches the primary key value
        passed to the id parameter

        Parameters
        ----------
        db: Session
            Instance of SQLAlchemy session that manages database transactions
        id: Any
            The primary key value of the row that will be deleted
        """
        record = db.get(self.model, id)
        db.delete(record)
        db.commit()
        return record

    def commit_changes(self, db: Session, record: ModelType) -> ModelType:
        """Adds changes to a session, commits them, and refreshes the record"""
        db.add(record)
        db.commit()
        db.refresh(record)  # issues a SELECT stmt to refresh values of record
        return record
