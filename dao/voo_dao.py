from models.voo import Voo

SQL_DELETA_VOO = 'delete from voo where Numero_voo = %s'
SQL_VOO_POR_NUMERO_VOO = 'SELECT Numero_voo, companhia_aerea, dias_semana from voo where Numero_voo = %s'
SQL_ATUALIZA_VOO = 'UPDATE voo SET companhia_aerea=%s, dias_semana=%s where Numero_voo = %s'
SQL_BUSCA_VOOS = 'SELECT Numero_voo, companhia_aerea, dias_semana from voo'
SQL_CRIA_VOO = 'INSERT into voo (companhia_aerea, dias_semana) values (%s, %s, %s)'


class VooDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, voo):
        cursor = self.__db.connection.cursor()

        if (voo.numero_voo):
            cursor.execute(SQL_ATUALIZA_VOO, (voo.companhia_aerea, voo.dias_semana, voo.numero_voo))
        else:
            cursor.execute(SQL_CRIA_VOO, (voo.companhia_aerea, voo.dias_semana))
            voo.numero_voo = cursor.lastrowid
        self.__db.connection.commit()
        return voo

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_VOOS)
        voos = traduz_voos(cursor.fetchall())
        return voos

    def busca_por_numero_voo(self, numero_voo):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_VOO_POR_NUMERO_VOO, (numero_voo,))
        tupla = cursor.fetchone()
        return Voo(tupla[1], tupla[2], tupla[3], id=tupla[0])

    def deletar(self, numero_voo):
        self.__db.connection.cursor().execute(SQL_DELETA_VOO, (numero_voo, ))
        self.__db.connection.commit()

def traduz_voos(voos):
    def cria_voo_com_tupla(tupla):
        return Voo(tupla[1], tupla[2], tupla[3], numero_voo=tupla[0])
    return list(map(cria_voo_com_tupla, voos))
