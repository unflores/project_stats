from src.config import build_settings, _dotenv_path


def test_build_settings(monkeypatch):
    assert (
        build_settings(_dotenv_path(), 'testing.env')['TESTING'] == 'True'
    ), 'properly sets settings values'

    monkeypatch.setenv('TESTING', 'False')
    assert (
        build_settings(_dotenv_path(), 'testing.env')['TESTING'] == 'False'
    ), 'overrides values in settings from ENV'

    assert (
        build_settings(_dotenv_path(), None)['TESTING'] == 'False'
    ), 'sets values from ENV when no dotfile exists'
