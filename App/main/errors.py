from . import main
from flask import render_template

@main.app_errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404