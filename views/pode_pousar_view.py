from models.pode_pousar import Pode_pousar
from flask import render_template, request, redirect, url_for
from dao.pode_pousar_dao import Pode_pousarDao
from dao.tipo_aeronave_dao import Tipo_aeronaveDao
from dao.aeroporto_dao import AeroportoDao
from main import db, app

pode_pousar_dao = Pode_pousarDao(db)
tipo_aeronave_dao = Tipo_aeronaveDao (db)
aeroporto_dao = AeroportoDao (db)

@app.route('/pode_pousar')
@app.route('/pode_pousar/<string:nome_tipo_aeronave>/<int:codigo_aeroporto>')
def pode_pousar(nome_tipo_aeronave=None, codigo_aeroporto=None):
    pode_pousar = pode_pousar_dao.listar()
    tipo_aeronaves = tipo_aeronave_dao.listar()
    aeroportos = aeroporto_dao.listar()
    if nome_tipo_aeronave==None and codigo_aeroporto==None:
        return render_template('pode_pousar.html', titulo='Pode Pousar', pode_pousar=pode_pousar, tipo_aeronaves=tipo_aeronaves, aeroportos=aeroportos)
    elif nome_tipo_aeronave and codigo_aeroporto:
        pode_pousar_escolhido = pode_pousar_dao.busca_por_nome_tipo_aeronave_por_codigo_aeroporto(nome_tipo_aeronave, codigo_aeroporto)
        return render_template('pode_pousar.html', titulo='Pode Pousar', pode_pousar=pode_pousar, tipo_aeronaves=tipo_aeronaves, aeroportos=aeroportos, pode_pousar_escolhido=pode_pousar_escolhido)
    else:
        return redirect(url_for('pode_pousar'))
        
@app.route('/criar_pode_pousar', methods=['POST',])
def criar_pode_pousar():
    nome_tipo_aeronave = request.form['nome_tipo_aeronave']
    codigo_aeroporto = request.form['codigo_aeroporto']
    pode_pousar = Pode_pousar(nome_tipo_aeronave, codigo_aeroporto)
    pode_pousar = pode_pousar_dao.salvar(pode_pousar)
    return redirect(url_for('pode_pousar'))

@app.route('/atualizar_pode_pousar', methods=['POST',])
def atualizar_pode_pousar():
    nome_tipo_aeronave = request.form['nome_tipo_aeronave']
    codigo_aeroporto = request.form['codigo_aeroporto']
    pode_pousar = Pode_pousar(nome_tipo_aeronave, codigo_aeroporto)
    nome_tipo_aeronave_escolhido = request.form['nome_tipo_aeronave_escolhido']
    codigo_aeroporto_escolhido = request.form['codigo_aeroporto_escolhido']
    pode_pousar_escolhido = Pode_pousar(nome_tipo_aeronave_escolhido, codigo_aeroporto_escolhido)
    pode_pousar_dao.atualizar(pode_pousar, pode_pousar_escolhido)
    return redirect(url_for('pode_pousar'))

@app.route('/deletar_pode_pousar/<string:nome_tipo_aeronave>/<int:codigo_aeroporto>')
def deletar_pode_pousar(nome_tipo_aeronave, codigo_aeroporto):
    pode_pousar_dao.deletar(nome_tipo_aeronave, codigo_aeroporto)
    return redirect(url_for('pode_pousar'))