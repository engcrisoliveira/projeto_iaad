from models.voo import Voo
from flask import render_template, request, redirect, url_for
from dao.voo_dao import VooDao
from main import db, app

voo_dao = VooDao(db)

@app.route('/voo')
@app.route('/voo/<int:id>')
def voo(id=None):
    voos = voo_dao.listar()
    if id:
        voo = voo_dao.busca_por_numero_voo(id)
        return render_template('voo.html', titulo='Editando Voo', voo=voo, voos=voos)
    else:
        return render_template('voo.html', titulo='Voo', voos=voos)
        
@app.route('/criar', methods=['POST',])
def criar_voo():
    companhia_aerea = request.form['companhia_aerea']
    dias_semana = request.form['dias_semana']
    voo = Voo(companhia_aerea, dias_semana)
    voo = voo_dao.salvar(voo)
    return redirect(url_for('voo'))

@app.route('/atualizar', methods=['POST',])
def atualizar_voo():
    companhia_aerea = request.form['companhia_aerea']
    dias_semana = request.form['dias_semana']
    voo = Voo(companhia_aerea, dias_semana, numero_voo=request.form['numero_voo'])
    voo_dao.salvar(voo)
    return redirect(url_for('voo'))

@app.route('/deletar/<int:id>')
def deletar_voo(id):
    voo_dao.deletar(id)
    return redirect(url_for('voo'))