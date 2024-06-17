def test_home_page(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the BMI Calculator" in response.data
    assert b"Login" in response.data
    assert b"Sign Up" in response.data
