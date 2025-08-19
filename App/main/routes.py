from flask import Blueprint, render_template, request, current_app
from . import main
import csv
import os

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
