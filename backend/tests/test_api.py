from app.main import app
from fastapi.testclient import (
    TestClient
)
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)


client = TestClient(app)


def test_root():

    response = client.get("/")

    assert response.status_code == 200


def test_profile_endpoint():

    response = client.get(
        "/profile/octocat"
    )

    assert response.status_code == 200
