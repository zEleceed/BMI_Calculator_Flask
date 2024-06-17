import pytest
from app.app import app as flask_app
from app.config import db
from app.models import User


@pytest.fixture(scope='module')
def app():
    yield flask_app


@pytest.fixture(scope='module')
def client(app):
    return app.test_client()


@pytest.fixture(scope='module')
def new_user():
    user = User(username='testuser', name='Test User')
    user.password_hash = "TestingIsGreat"
    return user


@pytest.fixture(scope='module')
def init_database(app):
    # Create the database and the database table
    db.create_all()

    default_user = User(username='testuser1', name='Test User1')
    default_user.password_hash = "FlaskIsHashed!"
    yield db
    db.drop_all()
