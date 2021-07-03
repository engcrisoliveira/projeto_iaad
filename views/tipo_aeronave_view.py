from models.tipo_aeronave import Tipo_aeronave
from flask import render_template, request, redirect, url_for
from dao.tipo_aeronave_dao import Tipo_aeronaveDao
from main import db, app

tipo_aeronave_dao = Tipo_aeronaveDao(db)

@app.route('/tipo_aeronave')
@app.route('/tipo_aeronave/<string:id>')
def tipo_aeronave(id=None):
    tipo_aeronaves = tipo_aeronave_dao.listar()
    if id:
        tipo_aeronave = tipo_aeronave_dao.busca_por_nome_tipo_aeronave(id)
        return render_template('tipo_aeronave.html', titulo='Editando Tipo da Aeronave', tipo_aeronave=tipo_aeronave, tipo_aeronaves=tipo_aeronaves)
    else:
        return render_template('tipo_aeronave.html', titulo='Tipo da Aeronave', tipo_aeronaves=tipo_aeronaves)
        
@app.route('/criar_tipo_aeronave', methods=['POST',])
def criar_tipo_aeronave():
    nome_tipo_aeronave = request.form['nome_tipo_aeronave']
    qtd_max_assentos = request.form['qtd_max_assentos']
    companhia = request.form['companhia']
    tipo_aeronave = Tipo_aeronave(nome_tipo_aeronave, qtd_max_assentos, companhia)
    tipo_aeronave = tipo_aeronave_dao.salvar(tipo_aeronave)
    return redirect(url_for('tipo_aeronave'))

@app.route('/atualizar_tipo_aeronave', methods=['POST',])
def atualizar_tipo_aeronave():
    # nome_tipo_aeronave = request.form['nome_tipo_aeronave']
    qtd_max_assentos = request.form['qtd_max_assentos']
    companhia = request.form['companhia']
    tipo_aeronave = Tipo_aeronave('teste', qtd_max_assentos, companhia)
    tipo_aeronave_dao.atualizar(tipo_aeronave)
    return redirect(url_for('tipo_aeronave'))

@app.route('/deletar_tipo_aeronave/<string:id>')
def deletar_tipo_aeronave(id):
    tipo_aeronave_dao.deletar(id)
    return redirect(url_for('tipo_aeronave'))