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


def test_login_page(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check that the response is valid
    """
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"Username" in response.data
    assert b"Password" in response.data


def test_signup_page(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/signup' page is requested (GET)
    THEN check that the response is valid
    """
    response = client.get("/signup")
    assert response.status_code == 200
    assert b"Name" in response.data
    assert b"Username" in response.data
    assert b"Password" in response.data
    assert b"Signup" in response.data


def test_login_attempt(client, init_database):
    """
     GIVEN a Flask application configured for testing
     WHEN the '/login' page is posted to with invalid credentials (POST)
     THEN check an error message is returned to the user
     """
    response = client.post("/login",
                           data=dict(username="123123", password="123123123123"),
                           follow_redirects=True)
    assert response.code == 400


