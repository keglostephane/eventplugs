import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')


class Development(Config):
    SQLALCHEMY_DATABASE_URI = (
        'postgresql://postgres:postgres@localhost:5432/'
        'eventplugs'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    BOOTSTRAP_SERVE_LOCAL = True
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse'


class Testing(Config):
    SQLALCHEMY_DATABASE_URI = (
        'postgresql://postgres:postgres@localhost:5432/'
        'test'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
