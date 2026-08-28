def test_update(auth_client, payload):

    response = auth_client.post("/booking", json=payload)
    assert response.status_code == 200
    booking_id = response.json()["bookingid"]

    response = auth_client.get(f"/booking/{booking_id}")
    assert response.status_code == 200

    payload["firstname"] = "Jurra"
    response = auth_client.put(f"/booking/{booking_id}", json=payload)
    assert response.status_code == 200

    response = auth_client.get(f"/booking/{booking_id}")
    assert response.status_code == 200
    assert response.json()["firstname"] == payload["firstname"]


def test_create_and_delete(auth_client, payload):

    response = auth_client.post("/booking", json=payload)
    assert response.status_code == 200
    booking_id = response.json()["bookingid"]

    response = auth_client.delete(f"/booking/{booking_id}")
    assert response.status_code == 201
    assert auth_client.get(f"/booking/{booking_id}").status_code == 404


def test_delete_without_auth(client, auth_client, payload):
    response = auth_client.post("/booking", json=payload)
    assert response.status_code == 200
    booking_id = response.json()["bookingid"]

    response = client.delete(f"/booking/{booking_id}")
    assert response.status_code == 403

    response = auth_client.delete(f"/booking/{booking_id}")
    assert response.status_code == 201
