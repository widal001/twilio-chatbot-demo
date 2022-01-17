from sqlalchemy.orm import Session

from chatbot.db import Base
import chatbot.models  # noqa: 401  -- prevents unused import error
from tests.utils.populate_db import populate_db

# make sure all SQL Alchemy models are imported (app.models) before initializing
# the DB, otherwise SQL Alchemy might fail to initialize relationships properly


def init_db(db: Session, testing: bool = False) -> None:
    """Initializes the database for unit testing or for alebic migrations

    Parameters
    ----------
    db: Session
        An instance of SessionLocal that creates the db engine and organizes
        calls to the database in a transaction
    testing: bool, optional
        Indicates whether to initialize the database in testing mode, which
        creates all of the tables from metadata instead of using Alembic.
        Default is to use Alembic migrations, see Notes below for details.

    Warning
    -------
    This function should only ever be called with testing=True during unit
    testing and the early stages of development. Doing so will create all of
    the tables from metadata. In all other cases (integration testing, QA
    testing, etc.) testing should remain False and tables should be created
    using Alembic migrations.
    """
    if testing:
        Base.metadata.drop_all(bind=db.get_bind())  # drop all existing tables
        Base.metadata.create_all(bind=db.get_bind())  # recreate all tables
        populate_db(db)  # add test data
