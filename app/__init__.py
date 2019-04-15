from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    
    app = Flask(__name__)
    
    # Create the app configurations
    app.config.from_object(config_options[config_name])
    
    
    # Initializing bootstrap
    bootstrap.init_app(app)
    
    
    # Registering Blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    
    # Setting up configuration
    from .requests import configure_request
    configure_request(app)
    
    
    return app

