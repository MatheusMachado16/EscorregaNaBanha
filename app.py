from flask import Flask, render_template

app = Flask(__name__)
# route ->
# função ->
# template 
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contatos")
def contatos():
    return render_template("contato.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

if __name__ == "__main__":
    app.run(debug=True)


