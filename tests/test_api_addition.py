def test_addition_success(client):
    response = client.post(
        "/calculate",
        json={"a": 5, "b": 3, "operation": "+"},
    )
    assert response.status_code == 200
    assert response.json() == {"result": 8}


def test_addition_with_zero(client):
    response = client.post(
        "/calculate",
        json={"a": 0, "b": 5, "operation": "+"},
    )
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_addition_negative_numbers(client):
    response = client.post(
        "/calculate",
        json={"a": -5, "b": -3, "operation": "+"},
    )
    assert response.status_code == 200
    assert response.json() == {"result": -8}
