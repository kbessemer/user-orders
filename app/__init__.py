from flask import Flask
from flask_migrate import Migrate
from .config import Config
from .database import db
import os
import importlib

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    controllers_dir = os.path.join(app.root_path, 'controllers')

    for filename in os.listdir(controllers_dir):
        module = importlib.import_module(f'.controllers.{filename}', package='app')

        if hasattr(module, 'blueprint'):
            app.register_blueprint(module.blueprint)

    return app
