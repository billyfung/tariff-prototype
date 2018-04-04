import pytest

from app import db, create_app
from config import TestConfig


@pytest.fixture(scope='session')
def app(request):
    # create the flask application
    from app import create_app
    app = create_app(config=TestConfig)
    db.init_app(app)
    ctx = app.app_context()
    # create application context
    ctx.push()
    request.addfinalizer(ctx.pop)

    return app


@pytest.fixture(scope='session')
def db(request):

    db.init_app = app

    def teardown():
        db.drop_all()

    db.create_all()


def test_app_name(app):
    assert app.name == 'volt'


@pytest.fixture(scope='session')
def test_client(request, app):
    client = app.test_client()
    client.__enter__()
    request.addfinalizer(
        lambda: client.__exit__(None, None, None))

    return client

class BasicTests(unittest.TestCase):
    # set up and teardown

    def setUp(self):
        app = create_app(config=TestConfig)

        self.app = app.test_client()

        db.drop_all()
        db.create_all()
