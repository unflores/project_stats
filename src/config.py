import os
from dotenv import dotenv_values

FLASK_ENV = os.getenv('FLASK_ENV', 'development')


def _dotenv_path():
    return os.path.join(os.path.dirname(__file__), '../envs')


def _get_env_file(env):
    if env == 'development':
        return 'development.env'
    elif env == 'testing':
        return 'testing.env'


def build_settings(envs_path, env_file):
    if env_file is None:
        env_settings = {
            key: '' for key in dotenv_values(os.path.join(envs_path, 'development.env'))
        }
    else:
        env_settings = {**dotenv_values(os.path.join(envs_path, env_file))}

    settings = {}

    for key, value in env_settings.items():
        settings[key] = os.getenv(key) if os.getenv(key) is not None else value
    return settings


settings = build_settings(_dotenv_path(), _get_env_file(FLASK_ENV))
