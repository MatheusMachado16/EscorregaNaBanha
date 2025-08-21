from . import main
from flask import render_template, current_app, request, redirect, url_for
from .models import Post
from App import db

@main.route("/", methods=['GET', 'POST'])
def index():
    from App.main.models import Post 
    if request.method == 'POST':
        title = request.form['title']
        email = request.form['email']
        content = request.form['content']
        novo_post = Post(title=title, email=email, content=content)
        db.session.add(novo_post)
        db.session.commit()

        return redirect(url_for('main.avaliacao'))
    return render_template("index.html")


@main.route("/avaliacoes", methods=['GET', 'POST'])
def avaliacao():
    posts = Post.query.all()
    return render_template('avaliacao.html', posts=posts)