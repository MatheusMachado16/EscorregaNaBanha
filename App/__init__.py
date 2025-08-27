from flask import Flask
from .main import main as main_bp


def create_app():
    app = Flask(__name__)
    app.secret_key = "minha_chave_secreta_super_segura_123"
    app.register_blueprint(main_bp)

    return app
