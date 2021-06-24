import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

    UPLOADED_PHOTOS_DEST ='app/static/photos'
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True



class ProdConfig(Config):
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://thirathenerd:admin2021@localhost/recipes'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}