from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_uploads import UploadSet,configure_uploads,IMAGES

bootstrap = Bootstrap()
photos = UploadSet('photos',IMAGES)

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')

    #configure UploadSet
    configure_uploads(app,photos)


    return app