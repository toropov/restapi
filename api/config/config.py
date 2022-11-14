import os
from decouple import config

class Config:
    SEKRET_KEY=config('SECRET_KEY', 'secret')

class DevConfig(Config):
    DEBUG=config('DEBUG', cast=bool)

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

config_dict={
    'dev':DevConfig,
    'prod':ProdConfig,
    'test':TestConfig
}