from flask import Flask, render_template, request, redirect, session, flash

class Jogos():
    def __init__(self, nome, genero, console):
        self.nome = nome
        self.genero = genero
        self.console = console

app = Flask(__name__)
app.secret_key = 'helloworld'

@app.route('/')
def inicio():
    return render_template('index.html', titulo="Jogos", jogos = lista)

jogo1 = Jogos('Fortnite', 'Battle Royale', 'PC')
jogo2 = Jogos('Spider-Man PS4', 'Ação', 'PS4')
jogo3 = Jogos('God of War', 'Ação', 'PS4')
lista = [jogo1, jogo2, jogo3]

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    return render_template('novo.html', titulo="Novo Jogo")

@app.route('/criar', methods = ['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogos(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods = ['POST',])
def autenticar():
    if '58214970' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(f'Usuário {session["usuario_logado"]} logado com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect(f'/{proxima_pagina}')
    else:
        flash("Usuário não logado!")
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash("Usuário deslogado com sucesso!")
    return redirect('/')

app.run(debug=True)