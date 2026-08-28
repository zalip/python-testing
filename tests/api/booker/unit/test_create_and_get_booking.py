def test_create_and_get_booking(auth_client):
    booking_payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {"checkin": "2018-01-01", "checkout": "2019-01-01"},
        "additionalneeds": "Breakfast",
    }

    post_result = auth_client.post("/booking", json=booking_payload)
    assert post_result.status_code == 200
    assert post_result.json()["bookingid"] is not None

    response = auth_client.get(f"/booking/{post_result.json()['bookingid']}")

    assert response.json() == booking_payload
