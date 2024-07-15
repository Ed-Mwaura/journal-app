import os 

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True 


class DevConfig(Config):
    DEVELOPMENT = True 
    DEGUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URI')


class ProdConfig(Config):
    DEVELOPMENT = False 
    DEGUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URI')

config = {
    'development': DevConfig,
    'prod': ProdConfig
}