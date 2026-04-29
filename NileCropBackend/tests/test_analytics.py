def test_analytics(client):
    response = client.get("/analytics/")

    assert response.status_code == 200
    data = response.json()

    assert "data" in data
    assert "total_crop_requests" in data["data"]
    assert "total_disease_requests" in data["data"]