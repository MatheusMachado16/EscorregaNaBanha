from . import main
from flask import Blueprint, render_template, current_app, request, flash, redirect, url_for
from datetime import datetime
import os
import csv


CSV_PATH = os.path.join(os.path.dirname(__file__), "..",
                        "static", "data", "posts.csv")
CSV_PATH = os.path.abspath(CSV_PATH)


def salvar_csv(title, email, content, data_envio):
    file_exists = os.path.isfile(CSV_PATH)
    with open(CSV_PATH, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Title', 'Email', 'Content'])
        writer.writerow([title, email, content, data_envio])


def ler_csv():
    posts = []
    if os.path.isfile(CSV_PATH):
        with open(CSV_PATH, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                posts.append(row)
    return posts


@main.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        email = request.form['email']
        content = request.form['comentario']
        data_envio = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        salvar_csv(title, email, content, data_envio)
        flash("Avaliação enviada!", "success")
        return redirect(url_for('main.index'))
    return render_template("index.html")


@main.route("/avaliacoes", methods=['GET'])
def avaliacao():
    posts = ler_csv()
    posts.reverse()
    return render_template('avaliacao.html', posts=posts)
