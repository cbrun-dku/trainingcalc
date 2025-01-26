def test_unsupported_operation(client):
    response = client.post(
        "/calculate",
        json={"a": 5, "b": 3, "operation": "%"},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Unsupported operation"}
