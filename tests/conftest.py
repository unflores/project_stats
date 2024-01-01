import pytest
import os
from src import create_app

@pytest.fixture()
def app():
    # Overriding the flask env here will allow for the testing
    # dot env to be loaded. See config
    os.environ['FLASK_ENV'] = 'testing'

    app = create_app()
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
