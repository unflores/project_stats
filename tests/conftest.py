import pytest
from src import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })


    # TODO: WHAT DO I NEED TO SET UP
    # HOW WILL dotenv work with this
    yield app

    # TODO WHAT DO I NEE TO TEAR DOWN?


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
