from models.tarifa import Tarifa
from flask import render_template, request, redirect, url_for
from dao.tarifa_dao import TarifaDao
from dao.voo_dao import VooDao
from main import db, app

tarifa_dao = TarifaDao(db)
voo_dao = VooDao (db)

@app.route('/tarifa')
@app.route('/tarifa/<int:id>')
def tarifa(id=None):
    tarifas = tarifa_dao.listar()
    voos = voo_dao.listar()
    if id:
        tarifa = tarifa_dao.buscar_tarifa_por_codigo(id)
        return render_template('tarifa.html', titulo='Editando Tarifa', tarifa=tarifa, tarifas=tarifas, voos=voos)
    else:
        return render_template('tarifa.html', titulo='Tarifa', tarifas=tarifas, voos=voos)
        
@app.route('/criar_tarifa', methods=['POST',])
def criar_tarifa():
    numero_voo = request.form['numero_voo']
    quantidade = request.form['quantidade']
    restricoes = request.form['restricoes']
    tarifa = Tarifa(numero_voo, quantidade, restricoes)
    tarifa = tarifa_dao.salvar(tarifa)
    return redirect(url_for('tarifa'))

@app.route('/atualizar_tarifa', methods=['POST',])
def atualizar_tarifa():
    numero_voo = request.form['numero_voo']
    quantidade = request.form['quantidade']
    restricoes = request.form['restricoes']
    codigo_tarifa = request.form['codigo_tarifa']
    tarifa = Tarifa(numero_voo, quantidade, restricoes, codigo_tarifa)
    tarifa_dao.salvar(tarifa)
    return redirect(url_for('tarifa'))

@app.route('/deletar_tarifa/<int:id>')
def deletar_tarifa(id):
    tarifa_dao.deletar(id)
    return redirect(url_for('tarifa'))