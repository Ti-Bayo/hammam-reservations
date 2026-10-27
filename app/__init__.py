from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev"  # à remplacer avant la mise en ligne

    from app.routes import bp
    app.register_blueprint(bp)

    return app