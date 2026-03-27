from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import criar_tabela, buscar_usuario, salvar_uniforme_banco
from models import Uniforme

app = Flask(__name__)
app.secret_key = "segredo123"  # necessário para session

#criar_tabela()

estoque = []

# 🔐 LOGIN
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('username')
        senha = request.form.get('password')

        user = buscar_usuario(usuario, senha)

        if user:
            session['usuario'] = usuario
            return redirect(url_for('painel'))
        else:
            return render_template('login.html', erro="Usuário ou senha inválidos")

    return render_template('login.html')


# 📊 PAINEL
@app.route('/painel')
def painel():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    return render_template('painel.html', estoque=estoque)


# ➕ CADASTRO
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        id = str(len(estoque) + 1)
        nome = request.form.get('nome')
        tamanho = request.form.get('tamanho')
        quantidade = int(request.form.get('quantidade'))
        setor = request.form.get('setor')

        novo_item = Uniforme(id, nome, tamanho, quantidade, setor)
        estoque.append(novo_item)

        return redirect(url_for('painel'))

    return render_template('cadastroUniforme.html')

@app.route('/cadastrar-uniforme', methods = ['POST'])
def cadastrar_uniforme():
    if request.method == 'POST':
        descricao = request.form.get('descricao')
        valor = request.form.get ('valor')
        quantidade = request.form.get('quantidade')

        try:
            salvar_uniforme_banco(descricao, valor, quantidade)
            flash (f"Uniforme cadastrado com sucesso")
        
        except Exception as e:
            flash (f"Erro  ao cadastrar: {e} ")
        
        return redirect (url_for('painel'))            

# 🚪 LOGOUT
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)