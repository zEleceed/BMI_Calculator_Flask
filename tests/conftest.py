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
def init_database(app):
    db.create_all()
    yield db
    db.drop_all()
