from models.instancia_trecho import Instancia_trecho
from flask import render_template, request, redirect, url_for
from dao.instancia_trecho_dao import Instancia_TrechoDao
from dao.voo_dao import VooDao
from dao.aeroporto_dao import AeroportoDao
from dao.aeronave_dao import AeronaveDao
from dao.trecho_voo_dao import Trecho_vooDao
from main import db, app

instancia_trecho_dao = Instancia_TrechoDao(db)
voo_dao = VooDao(db)
aeroporto_dao = AeroportoDao(db)
aeronave_dao = AeronaveDao(db)
trecho_voo_dao = Trecho_vooDao(db)

@app.route('/instancia_trecho')
@app.route('/instancia_trecho/<int:numero_voo>/<int:numero_trecho>/<string:dataa>')
def instancia_trecho(numero_voo=None, numero_trecho=None,dataa=None):
    instancia_trechos = instancia_trecho_dao.listar()
    voos = voo_dao.listar()
    aeroportos = aeroporto_dao.listar()
    aeronaves = aeronave_dao.listar()
    trecho_voos = trecho_voo_dao.listar()
    if numero_voo and numero_trecho and dataa:
        instancia_trecho = instancia_trecho_dao.buscar_instancia_pelo_numero_trecho(numero_voo, numero_trecho, dataa)
        return render_template('instancia_trecho.html', titulo='Instância Trecho', instancia_trechos=instancia_trechos, voos=voos, aeroportos=aeroportos, aeronaves=aeronaves, trecho_voos=trecho_voos, instancia_trecho=instancia_trecho)
    else:
        return render_template('instancia_trecho.html', titulo='Instância Trecho', instancia_trechos=instancia_trechos, voos=voos, aeroportos=aeroportos, aeronaves=aeronaves, trecho_voos=trecho_voos)
        
@app.route('/criar_instancia_trecho', methods=['POST',])
def criar_instancia_trecho():
    numero_voo = request.form['numero_voo']
    numero_trecho = request.form['numero_trecho']
    dataa = request.form['dataa']
    numero_assentos_disponiveis = request.form['numero_assentos_disponiveis']
    codigo_aeronave = request.form['codigo_aeronave']
    codigo_aeroporto_partida = request.form['codigo_aeroporto_partida']
    horario_partida = request.form['horario_partida_previsto']
    codigo_aeroporto_chegada = request.form['codigo_aeroporto_chegada']
    horario_chegada = request.form['horario_chegada_previsto']
    instancia_trecho = Instancia_trecho(numero_voo, numero_trecho, dataa, numero_assentos_disponiveis, codigo_aeronave, codigo_aeroporto_partida, horario_partida, codigo_aeroporto_chegada, horario_chegada)
    instancia_trecho = instancia_trecho_dao.salvar(instancia_trecho)
    return redirect(url_for('instancia_trecho'))

@app.route('/atualizar_instancia_trecho', methods=['POST',])
def atualizar_instancia_trecho():
    numero_voo = request.form['numero_voo']
    numero_trecho = request.form['numero_trecho']
    dataa = request.form['dataa']
    numero_assentos_disponiveis = request.form['numero_assentos_disponiveis']
    codigo_aeronave = request.form['codigo_aeronave']
    codigo_aeroporto_partida = request.form['codigo_aeroporto_partida']
    horario_partida = request.form['horario_partida_previsto']
    codigo_aeroporto_chegada = request.form['codigo_aeroporto_chegada']
    horario_chegada = request.form['horario_chegada_previsto']
    instancia_trecho = Instancia_trecho(numero_voo, numero_trecho, dataa, numero_assentos_disponiveis, codigo_aeronave, codigo_aeroporto_partida, horario_partida, codigo_aeroporto_chegada, horario_chegada)
    numero_voo_escolhido = request.form['numero_voo_escolhido']
    numero_trecho_escolhido = request.form['numero_trecho_escolhido']
    dataa_escolhido = request.form['dataa_escolhido']
    instancia_escolhida = Instancia_trecho(numero_voo_escolhido, numero_trecho_escolhido, dataa_escolhido, numero_assentos_disponiveis, codigo_aeronave, codigo_aeroporto_partida, horario_partida, codigo_aeroporto_chegada, horario_chegada)
    instancia_trecho = instancia_trecho_dao.atualizar(instancia_trecho, instancia_escolhida)
    return redirect(url_for('instancia_trecho'))

@app.route('/deletar_instancia_trecho/<int:numero_voo>/<int:numero_trecho>/<string:dataa>')
def deletar_instancia_trecho(numero_voo, numero_trecho, dataa):
    instancia_trecho_dao.deletar(numero_voo, numero_trecho, dataa)
    return redirect(url_for('instancia_trecho'))