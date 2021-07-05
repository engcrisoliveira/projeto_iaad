from dao.trecho_voo_dao import Trecho_vooDao
from dao.voo_dao import VooDao
from models.reserva_assento import Reserva_assento
from flask import render_template, request, redirect, url_for
from dao.reserva_assento_dao import Reserva_assentoDao
from main import db, app

reserva_assento_dao = Reserva_assentoDao(db)
voo_dao = VooDao (db)
trecho_voo_dao = Trecho_vooDao(db)

@app.route('/reserva_assento')
@app.route('/reserva_assento/<int:numero_voo>/<int:numero_trecho>/<string:dataa>/<int:numero_assento>')
def reserva_assento(numero_voo=None, numero_trecho=None, dataa=None, numero_assento=None):
    reservas = reserva_assento_dao.listar()
    voos = voo_dao.listar()
    trecho_voos = trecho_voo_dao.listar()
    if numero_voo and numero_trecho and dataa and numero_assento:
        reserva = reserva_assento_dao.buscar_reserva(numero_voo,numero_trecho,dataa,numero_assento)
        return render_template('reserva_assento.html', titulo='Editado Reserva Assento',
        voos=voos,trecho_voos=trecho_voos,  reserva = reserva, reservas=reservas)
    else:
        return render_template('reserva_assento.html', titulo='Reserva de Assentos',voos=voos,trecho_voos=trecho_voos, reservas=reservas)

@app.route('/criar_reserva_assento', methods=['POST',])
def criar_reserva_assento():
    numero_voo = request.form['numero_voo']
    numero_trecho = request.form['numero_trecho']
    dataa = request.form['dataa']
    numero_assento = request.form['numero_assento']
    nome_cliente = request.form['nome_cliente']
    telefone_cliente = request.form['telefone_cliente']
    reserva = Reserva_assento(
        Numero_voo = numero_voo,
        Numero_trecho = numero_trecho,
        Dataa = dataa,
        Numero_assento = numero_assento,
        Nome_cliente = nome_cliente,
        Telefone_cliente = telefone_cliente
    )
    reserva = reserva_assento_dao.salvar(reserva)
    return redirect(url_for('reserva_assento'))

@app.route('/atualizar_reserva_assento', methods=['POST'])
def atualizar_reserva_assento():
    numero_voo = request.form['numero_voo']
    numero_trecho = request.form['numero_trecho']
    dataa = request.form['dataa']
    numero_assento = request.form['numero_assento']
    nome_cliente = request.form['nome_cliente']
    telefone_cliente = request.form['telefone_cliente']
    reserva = Reserva_assento(
        Numero_voo = numero_voo,
        Numero_trecho = numero_trecho,
        Dataa = dataa,
        Numero_assento = numero_assento,
        Nome_cliente = nome_cliente,
        Telefone_cliente = telefone_cliente
    )
    numero_voo_escolhido = request.form['numero_voo_escolhido']
    numero_trecho_escolhido = request.form['numero_trecho_escolhido']
    dataa_escolhido = request.form['dataa_escolhido']
    numero_assento_escolhido = request.form['numero_assento_escolhido']
    reserva_escolhido = Reserva_assento(
        Numero_voo = numero_voo_escolhido,
        Numero_trecho = numero_trecho_escolhido,
        Dataa = dataa_escolhido,
        Numero_assento = numero_assento_escolhido,
        Nome_cliente = nome_cliente,
        Telefone_cliente = telefone_cliente
    )
    reserva_assento_dao.salvar(reserva,reserva_escolhido)
    return redirect(url_for('reserva_assento'))


@app.route('/deletar_reserva_assento/<int:numero_voo>/<int:numero_trecho>/<string:dataa>/<int:numero_assento>')
def deletar_reserva_assento(numero_voo,numero_trecho, dataa,numero_assento):
    reserva_assento_dao.deletar(numero_voo,numero_trecho,dataa, numero_assento)
    return redirect(url_for('reserva_assento'))


    