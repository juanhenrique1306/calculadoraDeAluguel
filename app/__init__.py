import os
from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    os.makedirs(app.config["EXPORT_DIR"], exist_ok=True)

    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    return app
