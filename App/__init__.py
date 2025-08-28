from flask import Flask
from .main import main as main_bp


def create_app():
    app = Flask(__name__)
    app.secret_key = 'sua_chave_secreta_aqui'
    app.register_blueprint(main_bp)

    return app
