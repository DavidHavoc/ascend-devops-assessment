import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.storage import store


@pytest.fixture(autouse=True)
def _reset_store():
    """Reload data before each test so tests stay independent."""
    store.reset()
    yield


@pytest.fixture
def client():
    return TestClient(app)
