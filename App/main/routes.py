from flask import render_template, request, current_app
from . import main
import csv
import os

@main.route("/")
def index():
    posts = current_app.posts
    return render_template("index.html", posts=posts)
@main.route("/sobre")
def sobre():
    return render_template("sobre.html")

notas = []
@main.route("/avaliacoes", methods=['GET', 'POST'])
def avaliacao():
    media = None
    if request.method == 'POST':
        try:
            nota = float(request.form.get('nota1'))
            notas.append(nota)
            notarestaurante = request.form.get('nota2', type=int)
            media = round(sum(notas)/len(notas), 2)
        except ValueError:
            media = 'Error: entradas inválidas'
    return render_template('avaliacao.html', media=media)

def carregar_produtos():
    produtos = []
    caminho_csv = os.path.join(current_app.root_path, 'static', 'data', 'produtos.csv')
    with open(caminho_csv, newline='', encoding='utf-8') as f:
        linhas = f.readlines()
        for linha in linhas[1:]:  # pula o cabeçalho
            categoria, nome, descricao, foto, preco = linha.strip().split(',')
            produtos.append({
                'categoria': categoria,
                'nome': nome,
                'descricao': descricao,
                'foto': foto,
                'preco': float(preco)
            })
    return produtos

@main.route("/cardapio")
def cardapio():
    produtos = carregar_produtos()
    pratos = [p for p in produtos if p['categoria'] == 'prato']
    porcoes = [p for p in produtos if p['categoria'] == 'porcao']
    bebidas = [p for p in produtos if p['categoria'] == 'bebida']
    return render_template("cardapio.html", pratos=pratos, bebidas=bebidas, porcoes=porcoes)

# @main.route("/base")
# def base():
#     return render_template("base.html")
