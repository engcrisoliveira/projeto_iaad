from models.lista_assentos import ListaAssentos

CALL_STORED_PROCEDURE = 'CALL verAssento(%s)'

class StoredProcedure:
    def __init__(self, db):
        self.__db = db

    def execute(self, cliente):
        cursor = self.__db.connection.cursor()
        cursor.execute(CALL_STORED_PROCEDURE, (cliente, ))
        assentos = []
        for tupla in cursor.fetchall():
            assentos.append(tupla[0])
        listaAssentos = ListaAssentos(assentos)
        return listaAssentos