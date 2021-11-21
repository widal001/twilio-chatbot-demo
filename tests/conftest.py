import pytest
from fastapi.testclient import TestClient

from chatbot import app


@pytest.fixture(scope="session", name="mock_client")
def fixture_client():
    """Exposes a mock client for api unit tests"""
    return TestClient(app)
