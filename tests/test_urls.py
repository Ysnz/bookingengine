import pytest


@pytest.mark.urls("booking_engine.urls")
def test_urls_client(client):
    response = client.get("/api/v1/health_check/")
    assert response.content == b"Success!"
