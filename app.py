from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    fruta1:str = "Morango" # pode ser via banco ou requisicao
    fruta2: str = "Uva" # aqui tambem poode ser via banco ou requisicao
    lista_frutas = ["Morango","Uva","Mamao","Maca"]
    return render_template("index.html",frutas = lista_frutas) # fazendo assim podemos usar a variavel no html

@app.route('/sobre')
def sobre():
    notas = {"Fulano":5.0, "Beltrano":6.0, "Aluno:":7.0,"Sicrano":8.5}
    return render_template("sobre.html",notas=notas)

