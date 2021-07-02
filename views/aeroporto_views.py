from models.aeroporto import Aeroporto
from flask import render_template, request, redirect, flash, url_for
from dao.aeroporto_dao import AeroportoDao
from main import db, app

aeroporto_dao = AeroportoDao(db)

@app.route('/aeroporto')
@app.route('/aeroporto/<int:id>')
def aeroporto(id=None):
    aeroportos = aeroporto_dao.listar()
    if id:
        aeroporto = aeroporto_dao.busca_por_codigo_aeroporto(id)
        return render_template('aeroporto.html', titulo='Editando Aeroporto', aeroporto=aeroporto, aeroportos=aeroportos)
    else:
        return render_template('aeroporto.html', titulo='Aeroporto', aeroportos=aeroportos)
        
@app.route('/criar', methods=['POST',])
def criar_aeroporto():
    nome = request.form['nome']
    cidade = request.form['cidade']
    estado = request.form['estado']
    aeroporto = Aeroporto(nome, cidade, estado)
    aeroporto = aeroporto_dao.salvar(aeroporto)
    return redirect(url_for('aeroporto'))

@app.route('/atualizar', methods=['POST',])
def atualizar_aeroporto():
    nome = request.form['nome']
    cidade = request.form['cidade']
    estado = request.form['estado']
    aeroporto = Aeroporto(nome, cidade, estado, codigo_aeroporto=request.form['codigo_aeroporto'])
    aeroporto_dao.salvar(aeroporto)
    return redirect(url_for('aeroporto'))

@app.route('/deletar/<int:id>')
def deletar_aeroporto(id):
    aeroporto_dao.deletar(id)
    return redirect(url_for('aeroporto'))