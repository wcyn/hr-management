import os

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class Development(Config):
    DEBUG = True

class Staging(Config):
    DEBUG = True

class Production(Config):
    DEBUG = False

class Testing(object):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgres://localhost/test_hr"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app_config = {
    'development': Development,
    'staging': Staging,
    'production': Production,
    'testing': Testing
}