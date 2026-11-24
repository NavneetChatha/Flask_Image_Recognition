

import pytest
from app import app  # This imports the Flask app for testing

@pytest.fixture
def client():
    app.config["WTF_CSRF_ENABLED"] = False
    with app.test_client() as client:
        yield client
