from flasgger import Swagger
from flask import Flask
from app.routes import deposit_api


def create_app() -> Flask:
    app = Flask(__name__)
    swagger = Swagger(app, template_file='swagger.yml')
    app.register_blueprint(deposit_api)
    return app
