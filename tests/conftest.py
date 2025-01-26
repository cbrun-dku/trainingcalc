import pytest
from fastapi.testclient import TestClient
from trainingcalc.api import app
from trainingcalc.calculator import Calculator


@pytest.fixture(scope="session")
def calc():
    return Calculator()


@pytest.fixture(scope="session")
def client():
    """Fixture to provide a TestClient for the FastAPI app."""
    return TestClient(app)