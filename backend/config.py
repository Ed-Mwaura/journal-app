import os 


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True 


class DevConfig(Config):
    DEVELOPMENT = True 
    SECRET_KEY = 'DEV'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')
    

class ProdConfig(Config):
    DEVELOPMENT = False 
    DEGUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')