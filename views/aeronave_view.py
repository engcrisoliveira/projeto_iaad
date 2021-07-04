from dao.tipo_aeronave_dao import Tipo_aeronaveDao
from models.aeronave import Aeronave
from flask import render_template, request, redirect, url_for
from dao.aeronave_dao import AeronaveDao
from main import db, app

aeronave_dao = AeronaveDao(db)
tipo_dao = Tipo_aeronaveDao(db)
@app.route('/aeronave')
@app.route('/aeronave/<int:id>')
def aeronave(id=None):
    aeronaves = aeronave_dao.listar()
    tipos = tipo_dao.listar()
    if id:
        aeronave = aeronave_dao.busca_por_codigo_aeronave(id)
        return render_template('aeronave.html', titulo='Editando Aeronave', aeronave=aeronave, aeronaves=aeronaves)
    else:
        return render_template('aeronave.html',  titulo='Aeronave',tipos= tipos, aeronaves= aeronaves)

@app.route('/criar_aeronave', methods=['POST',])
def criar_aeronave():
    numero_total_assentos = request.form['numero_total_assentos']
    tipo_aeronave = request.form['tipo_aeronave']
    aeronave = Aeronave(numero_total_assentos = numero_total_assentos, tipo_aeronave=tipo_aeronave)
    aeronave = aeronave_dao.salvar(aeronave)
    return redirect(url_for('aeronave'))

@app.route('/atualizar_aeronave', methods=['POST',])
def atualizar_aeronave():
    nome = request.form['nome']
    cidade = request.form['cidade']
    estado = request.form['estado']
    aeronave = Aeronave(nome, cidade, estado, codigo_aeronave=request.form['codigo_aeronave'])
    aeronave_dao.salvar(aeronave)
    return redirect(url_for('aeronave'))

@app.route('/deletar_aeronave/<int:id>')
def deletar_aeronave(id):
    aeronave_dao.deletar(id)
    return redirect(url_for('aeronave'))