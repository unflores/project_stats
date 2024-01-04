from src.config import build_settings, _dotenv_path


def test_build_settings(monkeypatch):
    assert 'properly sets settings values', (
        build_settings(_dotenv_path(), 'testing.env')['TESTING'] == 'True'
    )

    monkeypatch.setenv('TESTING', 'False')
    assert 'overrides values in settings from ENV', (
        build_settings(_dotenv_path(), 'testing.env')['TESTING'] == 'False'
    )
