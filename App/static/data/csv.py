# TEMPORARIO!!!! SO PARA VER COMO FUNCIONA PYTHON E CSV
import csv

def carregar_produtos():
    produtos = []
    with open('produtos.csv', newline='', encoding='utf-8') as f:
        linhas = f.readlines()
        for linha in linhas[1:]:  # pula o cabeçalho
            nome, descricao, foto, preco = linha.strip().split(',')
            produtos.append({
                'nome': nome,
                'descricao': descricao,
                'foto': foto,
                'preco': float(preco)
            })
    return produtos
# @app.route('/catalogo')
def catalogo():
    produtos = carregar_produtos
    return render_template('catalogo.html', produtos = produtos)