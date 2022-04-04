from flask import Flask, render_template, request

class Jogo:
    def __init__(self, nome, categoria, console, ano):
        self.nome = nome
        self.categoria = categoria
        self.console = console
        self.ano = ano

jogo1 = Jogo('Age of Empires', 'RTS', 'PC', '1995')
jogo2 = Jogo('Diablo 3', 'RPG', 'PC', '2021')
jogo3 = Jogo('Zelda', 'RPG', 'SNES', '1990' )
jogo4 = Jogo('Super Mario World', 'Plataforma', 'SNES', '1991')
jogo5 = Jogo('Top Gear', 'Corrida', 'SNES', '1992')
lista = [jogo1, jogo2, jogo3, jogo4, jogo5]

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('lista.html', titulo="jogosflix", jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='novo jogo: ')

@app.route('/criar', methods=['POST'])
def criar ():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    ano = request.form['ano']
    jogo = Jogo(nome, categoria, console, ano)
    lista.append(jogo)

    return render_template('lista.html', titulo="jogos", jogos=lista)

app.run(debug=True)