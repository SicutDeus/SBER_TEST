from flask import Flask

from app.routes import deposit_api


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(deposit_api)
    return app
