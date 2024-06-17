from app.models import User
from app.config import db


def test_new_user(new_user):
    """
        GIVEN a User model
        WHEN a new User is created
        THEN check the username, name, are defined correctly
    """
    assert new_user.username == "testuser"
    assert new_user.name == "Test User"


def test_new_user_hashing_password(new_user):
    """
        GIVEN a User model
        WHEN the password is set
        THEN check the password is hashed correctly and not stored as plaintext
    """
    new_user.password_hash = 'TestingIsGreat'
    assert new_user._password_hash != 'TestingIsGreat'  # Ensure the password is hashed


def test_user_authenticated(new_user):
    """
        GIVEN an existing user model
        WHEN the password is set and authenticated
        THEN check if the password is correct for the user
    """
    new_user.password_hash = "TestingIsAwesomeeeee"
    assert new_user.authenticate("TestingIsAwesomeeeee")
    assert not new_user.authenticate("Fake")


def test_serialization_rules(new_user):
    """
        GIVEN an existing user
        WHEN a user is serialized into dict type
        THEN check if the password hash is included in the output
    """
    new_user.password_hash = "TestSerialize"
    user_dict = new_user.to_dict()
    assert "_password_hash" not in user_dict