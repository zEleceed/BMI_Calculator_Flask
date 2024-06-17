from app.models import User
from app.config import db


def test_new_user(new_user):
    """
        GIVEN a User model
        WHEN a new User is created
        THEN check the username, name, and password_hash fields are defined correctly
    """
    assert new_user.username == "testuser"
    assert new_user.name == "Test User"
    assert new_user._password_hash != "TestingIsGreat"  # Ensure the password is hashed
    assert new_user.authenticate("TestingIsGreat")



