from flask import Flask
from .config import Config
from .models import mongo_db_instance
from .routes import bp as routes_bp
from .utils import load_csv_data

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the MongoDB instance
    mongo_db_instance.client = mongo_db_instance.client

    with app.app_context():
        load_csv_data()  # Load data into MongoDB

    app.register_blueprint(routes_bp)

    return app
