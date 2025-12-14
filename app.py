from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    nome:str = "fulano" # pode ser via banco ou requisicao
    idade: float = 25 # aqui tambem poode ser via banco ou requisicao
    return render_template("index.html", nome=nome, idade=idade) # fazendo assim podemos usar a variavel no html

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")

