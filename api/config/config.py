import os
from decouple import config
from datetime import timedelta

class Config:

# ключи создаются в интерпретаторе
# >>> import secrets
# >>> secrets.token.hex(12)

    SECRET_KEY=config('SECRET_KEY','Secret')
    JWT_SECRET_KEY=config('JWT_SECRET_KEY')    
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(minutes=30)


BASE_DIR=os.path.dirname(os.path.realpath(__file__))

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(BASE_DIR,'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True
    DEBUG=True

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

config_dict={
    'dev':DevConfig,
    'prod':ProdConfig,
    'test':TestConfig
}