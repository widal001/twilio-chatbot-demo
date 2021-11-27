# pylint: disable=C0103,W0613
import pytest
from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from chatbot import app
from chatbot.database import Base
from chatbot.config import settings
from tests.utils.populate_db import populate_db


@pytest.fixture(scope="session", name="mock_client")
def fixture_client():
    """Exposes a mock client for api unit tests"""
    return TestClient(app)


@pytest.fixture(scope="session", name="test_config")
def fixture_config():
    """Returns the configuration settings for use in tests"""
    return settings.from_env("testing")


@pytest.fixture(scope="session", name="test_session")
def fixture_db(mock_client, test_config):
    """Creates a local database for unit testing"""
    local_db = test_config.database_url
    engine = create_engine(
        local_db,
        connect_args={"check_same_thread": False},
    )
    Base.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )
    try:
        with TestingSessionLocal() as session:
            populate_db(session)
            yield session
    except Exception as error:
        raise error
    finally:
        Base.metadata.drop_all(bind=engine)
