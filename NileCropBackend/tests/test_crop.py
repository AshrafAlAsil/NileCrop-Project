def test_crop_request(client):
    response = client.post("/crop/crop-request", json={
        "city": "Cairo",
        "temperature": 30,
        "humidity": 50,
        "soil_type": "clay"
    })

    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "data" in data
    assert "recommended_crop" in data["data"]