from App import create_app
from flask import Flask
from App.main import main as main_blueprint


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
