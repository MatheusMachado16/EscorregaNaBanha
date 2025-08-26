# from flask import Flask
# from .main import main as main_bp


# def create_app():
#     app = Flask(__name__)
#     app.register_blueprint(main_bp)

#     return app

from flask import Flask
from .main import main as main_bp

def create_app():
    # Define onde estão os templates e arquivos estáticos
    app = Flask(__name__, template_folder="App/templates", static_folder="App/static")
    
    # Registra o blueprint
    app.register_blueprint(main_bp)

    return app