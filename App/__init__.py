from flask import Flask
from .main import main as main_bp
from .admin import admin as admin_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret'
    app.posts = []  # lista simulando "banco de dados"

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app