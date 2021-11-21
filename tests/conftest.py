import pytest
from fastapi.testclient import TestClient

from chatbot import app
from chatbot.examples.classes import Person


@pytest.fixture(scope="function")
def alice():
    """Returns a sample instance of the Person which gets recreated
    for every pytest function. This instance has the following attributes:
        first_name: Alice
        last_name: Doe
        age: 35
    """
    return Person("Alice", "Doe", 35)


@pytest.fixture(scope="session", name="mock_client")
def fixture_client():
    """Exposes a mock client for api unit tests"""
    return TestClient(app)
