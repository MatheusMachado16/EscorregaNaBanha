from flask import render_template, current_app, Flask, request, session
from . import main

# @main.route('/')
# def index():
#     posts = current_app.posts
#     return render_template('index.html', posts=posts)

@main.route("/")
def index():
    posts = current_app.posts
    return render_template("index.html", posts=posts)

@main.route("/sobre")
def sobre():
    return render_template("sobre.html")

@main.route("/avaliacoes")
def avaliacao():
    return render_template("avaliacao.html")

@main.route("/cardapio")
def cardapio():
    return render_template("cardapio.html")

@main.route("/base")
def base():
    return render_template("base.html")
