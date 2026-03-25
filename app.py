from flask import Flask, render_template, request
from models import Uniforme

app = Flask (__name__)

estoque = []

@app.route('/')
def index ():
    return render_template ('login.html', estoque = estoque)

@app.route ('/cadastrar', methods=['POST'])
def cadastrar():
    id=str(len(estoque)+1)
    nome = request.form.get('nome')
    tamanho = request.form.get('tamanho')
    quantidade = int(request.form.get('quantidade'))
    setor = request.form.get('setor')

    novo_item  = Uniforme (id, nome, tamanho, quantidade, setor)
    estoque.append(novo_item)

    return render_template('cadastro.html', estoque=estoque, mensagem= "cadastro realizado com sucesso!")








if __name__ == '__main__':
    app.run(debug=True)