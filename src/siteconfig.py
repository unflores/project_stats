import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '../envs')

FLASK_ENV = os.getenv('FLASK_ENV', 'development')


def get_env_file(env):
    if env == 'development':
        return 'development.env'
    elif env == 'testing':
        return 'testing.env'


load_dotenv(os.path.join(dotenv_path, get_env_file(FLASK_ENV)))

# TODO Make this less annoying
SECRET_KEY = os.getenv('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
