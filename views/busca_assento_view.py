from flask import render_template, request, redirect, url_for
from dao.stored_procedure import StoredProcedure
from models.lista_assentos import ListaAssentos
from main import db, app

storedProcedure = StoredProcedure(db)

@app.route('/buscar_assento')
@app.route('/buscar_assento')
def buscar_assento():
    cliente = request.args.get('cliente')
    if cliente:
        listaAssentos = storedProcedure.execute(cliente)
    else:
        listaAssentos = ListaAssentos([])
    return render_template('busca_assento.html', title='Buscar Assento', listaAssentos=listaAssentos)