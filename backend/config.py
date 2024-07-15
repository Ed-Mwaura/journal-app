import os 


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True 


class DevConfig(Config):
    DEVELOPMENT = True 
    SECRET_KEY = 'DEV'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')
    print('haha',SQLALCHEMY_DATABASE_URI)
    # SQLALCHEMY_DATABASE_URI = 'postgresql://admindev:admindev@localhost:5432/journal_dev'


class ProdConfig(Config):
    DEVELOPMENT = False 
    DEGUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')