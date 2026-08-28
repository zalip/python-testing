import httpx
import pytest

BASE = "https://restful-booker.herokuapp.com"
USERNAME = "admin"
PASSWORD = "password123"


@pytest.fixture(scope="session")
def client():
    with httpx.Client(base_url=BASE, timeout=30.0) as c:
        yield c


@pytest.fixture(scope="session")
def auth_client():
    with httpx.Client(base_url=BASE, timeout=30.0) as auth_client:
        auth_response = auth_client.post(
            "/auth", json={"username": USERNAME, "password": PASSWORD}
        )
        assert auth_response.status_code == 200
        auth_client.headers["Cookie"] = f"token={auth_response.json()['token']}"
        auth_client.headers["Accept"] = "application/json"
        auth_client.headers["Content-Type"] = "application/json"
        yield auth_client


@pytest.fixture
def payload():
    return {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {"checkin": "2018-01-01", "checkout": "2019-01-01"},
        "additionalneeds": "Breakfast",
    }
