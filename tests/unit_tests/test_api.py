def test_api(mock_client):
    """Checks the `GET /` route

    Validates the following conditions:
    - The status returned is 200
    - The response data returned is "Hello Word"
    """
    # execution
    response = mock_client.get("/")
    # validation
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
