from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from .database import db
from .controllers.Items import items
from .controllers.Orders import orders
from .controllers.Users import users

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    migrate = Migrate(app, db)

    from .models.item import Item
    from .models.order import Order
    from .models.user import User

    app.register_blueprint(items)
    app.register_blueprint(orders)
    app.register_blueprint(users)

    return app
