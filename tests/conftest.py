# pylint: disable=C0103,W0613
import pytest
from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from chatbot import app, db, config


@pytest.fixture(scope="session", name="test_config")
def fixture_config():
    """Returns the configuration settings for use in tests"""
    return config.settings.from_env("testing")


@pytest.fixture(scope="function", name="test_session")
def fixture_session(test_config):
    """Creates a local database for unit testing"""
    # TODO: Replace this code with yield db.session.SessionLocal()
    # after figuring out how to inject testing configurations
    engine = create_engine(
        test_config.database_url,
        pool_pre_ping=True,
        connect_args={"check_same_thread": False},
    )
    TestSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    with TestSession() as session:
        db.init_db(session, testing=True)
        yield session


@pytest.fixture(scope="function", name="mock_client")
def fixture_client(test_session):
    """Exposes a mock client for api unit tests"""

    def override_get_db():
        """Overrides the get_db() dependency to yield a test session"""
        yield test_session

    app.dependency_overrides[db.get_db] = override_get_db
    yield TestClient(app)
    del app.dependency_overrides[db.get_db]  # restores get_db() dependency
