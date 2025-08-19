from . import main
from flask import render_template

@main.route("/sobre")
def sobre():
    return render_template("sobre.html")