from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .main import main as main_bp
    app.register_blueprint(main_bp)
    
    with app.app_context():
        from App.main import models
        db.create_all()  # Cria as tabelas


    return app