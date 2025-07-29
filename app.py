from flask import Flask, render_template, request, session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/avaliacoes")
def avaliacao():
    return render_template("avaliacao.html")

@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html")

@app.route("/base")
def base():
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=True)