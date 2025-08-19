from . import main
from flask import render_template, current_app, request

@main.route("/")
def index():
    posts = current_app.posts
    return render_template("index.html", posts=posts)

notas = []
@main.route("/avaliacoes", methods=['GET', 'POST'])
def avaliacao():
    media = None
    if request.method == 'POST':
        try:
            nota = float(request.form.get('nota1'))
            notas.append(nota)
            media = round(sum(notas)/len(notas), 2)
        except ValueError:
            media = 'Error: entradas inválidas'
    return render_template('avaliacao.html', media=media)