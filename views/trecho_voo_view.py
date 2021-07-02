from models.trecho_voo import Trecho_voo
from flask import render_template, request, redirect, url_for
from dao.trecho_voo_dao import Trecho_vooDao
from dao.voo_dao import VooDao
from dao.aeroporto_dao import AeroportoDao
from main import db, app

trecho_voo_dao = Trecho_vooDao(db)
voo_dao = VooDao (db)
aeroporto_dao = AeroportoDao (db)

@app.route('/trecho_voo')
@app.route('/trecho_voo/<int:id>')
def trecho_voo(id=None):
    trecho_voos = trecho_voo_dao.listar()
    voos = voo_dao.listar()
    aeroportos = aeroporto_dao.listar()
    if id:
        trecho_voo = trecho_voo_dao.busca_por_numero_trecho(id)
        return render_template('trecho_voo.html', titulo='Editando Trecho do Voo', trecho_voo=trecho_voo, trecho_voos=trecho_voos, voos=voos, aeroportos=aeroportos)
    else:
        return render_template('trecho_voo.html', titulo='Trecho do Voo', trecho_voos=trecho_voos, voos=voos, aeroportos=aeroportos)
        
@app.route('/criar_trecho_voo', methods=['POST',])
def criar_trecho_voo():
    numero_voo = request.form['numero_voo']
    codigo_aeroporto_partida = request.form['codigo_aeroporto_partida']
    horario_partida_previsto = request.form['horario_partida_previsto']
    codigo_aeroporto_chegada = request.form['codigo_aeroporto_chegada']
    horario_chegada_previsto = request.form['horario_chegada_previsto']
    trecho_voo = Trecho_voo(numero_voo, codigo_aeroporto_partida, horario_partida_previsto, codigo_aeroporto_chegada, horario_chegada_previsto)
    trecho_voo = trecho_voo_dao.salvar(trecho_voo)
    return redirect(url_for('trecho_voo'))

@app.route('/atualizar_trecho_voo', methods=['POST',])
def atualizar_trecho_voo():
    numero_voo = request.form['numero_voo']
    codigo_aeroporto_partida = request.form['codigo_aeroporto_partida']
    horario_partida_previsto = request.form['horario_partida_previsto']
    codigo_aeroporto_chegada = request.form['codigo_aeroporto_chegada']
    horario_chegada_previsto = request.form['horario_chegada_previsto']
    trecho_voo = Trecho_voo(numero_voo, codigo_aeroporto_partida, horario_partida_previsto, codigo_aeroporto_chegada, horario_chegada_previsto, numero_trecho=request.form['numero_trecho'])
    trecho_voo_dao.salvar(trecho_voo)
    return redirect(url_for('trecho_voo'))

@app.route('/deletar_trecho_voo/<int:id>')
def deletar_trecho_voo(id):
    trecho_voo_dao.deletar(id)
    return redirect(url_for('trecho_voo'))