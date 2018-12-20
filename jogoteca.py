from flask import Flask, render_template, request
from flask import redirect, session, flash, url_for
from jogo import Jogo
from usuario import Usuario


app = Flask(__name__)


usuario1 = Usuario('luan', 'Luiz Antonio Marques', '1234')
usuario2 = Usuario('Nico', 'Nico Steppat', '7a1')
usuario3 = Usuario('flavio', 'flavio Almeida', 'javascript')

usuarios = {usuario1.id: usuario1, 
            usuario2.id: usuario2, 
            usuario3.id: usuario3}


jogo1 = Jogo('Tetris', 'Puzzle', 'Game Boy')
jogo2 = Jogo('Tetris', 'Puzzle', 'Game Boy')
jogo3 = Jogo('Tetris', 'Puzzle', 'Game Boy')
lista = [jogo1, jogo2, jogo3]
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('novo'))) 
    return render_template('novo.html', titulo='Adicionar Novo Jogo')


@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template(
        'login.html', titulo='Faça seu Login', proxima=proxima
        )


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Não logou, tente denovo!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('index'))


app.run(debug=True, host='0.0.0.0', port='8080')
