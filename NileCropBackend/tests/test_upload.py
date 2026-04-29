import io

def test_upload_image(client):
    file = io.BytesIO(b"fake image content")

    response = client.post(
        "/upload/upload-image",
        files={"file": ("test.jpg", file, "image/jpeg")}
    )

    assert response.status_code == 200
    data = response.json()
    assert "filename" in data
    assert "prediction" in data