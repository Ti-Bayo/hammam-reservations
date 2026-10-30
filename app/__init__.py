import os
from flask import Flask
from app.models import db


def create_app(config=None):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hammam.db"
    if config:
        app.config.update(config)

    db.init_app(app)

    from app.routes import bp
    app.register_blueprint(bp)

    from app.api import api
    app.register_blueprint(api)

    from app.donnees import init_db_command
    app.cli.add_command(init_db_command)

    return app