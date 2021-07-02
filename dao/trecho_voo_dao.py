from models.trecho_voo import Trecho_voo

SQL_DELETA_TRECHO_VOO = 'delete from TRECHO_VOO where Numero_trecho = %s'
SQL_TRECHO_VOO_POR_NUMERO_TRECHO = 'SELECT Numero_trecho, Codigo_aeroporto_partida, Horario_partida_previsto, Codigo_aeroporto_chegada, Horario_chegada_previsto from TRECHO_VOO where Numero_trecho = %s'
SQL_ATUALIZA_TRECHO_VOO = 'UPDATE TRECHO_VOO SET Numero_voo=%s, Codigo_aeroporto_partida=%s, Horario_partida_previsto=%s, Codigo_aeroporto_chegada=%s, Horario_chegada_previsto=%s where Numero_trecho = %s'
SQL_BUSCA_TRECHO_VOOS = 'SELECT Numero_voo, Numero_trecho, Codigo_aeroporto_partida, Horario_partida_previsto, Codigo_aeroporto_chegada, Horario_chegada_previsto from TRECHO_VOO'
SQL_CRIA_TRECHO_VOO = 'INSERT into TRECHO_VOO (Numero_voo, Codigo_aeroporto_partida, Horario_partida_previsto, Codigo_aeroporto_chegada, Horario_chegada_previsto) values (%s, %s, %s, %s, %s)'


class Trecho_vooDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, trecho_voo):
        cursor = self.__db.connection.cursor()

        if (trecho_voo.numero_trecho):
            cursor.execute(SQL_ATUALIZA_TRECHO_VOO, (trecho_voo.numero_trecho, trecho_voo.codigo_aeroporto_partida, trecho_voo.horario_partida_previsto, trecho_voo.codigo_aeroporto_chegada, trecho_voo.horario_chegada_previsto, trecho_voo.numero_trecho))
        else:
            cursor.execute(SQL_CRIA_TRECHO_VOO, (trecho_voo.numero_voo, trecho_voo.codigo_aeroporto_partida, trecho_voo.horario_partida_previsto, trecho_voo.codigo_aeroporto_chegada,trecho_voo.horario_chegada_previsto))
            trecho_voo.numero_trecho = cursor.lastrowid
        self.__db.connection.commit()
        return trecho_voo

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_TRECHO_VOOS)
        trecho_voos = traduz_trecho_voos(cursor.fetchall())
        return trecho_voos

    def busca_por_numero_trecho(self, numero_trecho):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_TRECHO_VOO_POR_NUMERO_TRECHO, (numero_trecho,))
        tupla = cursor.fetchone()
        return Trecho_voo(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], numero_trecho=tupla[0])

    def deletar(self, numero_trecho):
        self.__db.connection.cursor().execute(SQL_DELETA_TRECHO_VOO, (numero_trecho, ))
        self.__db.connection.commit()

def traduz_trecho_voos(trecho_voos):
    def cria_trecho_voo_com_tupla(tupla):
        return Trecho_voo(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], numero_trecho=tupla[0])
    return list(map(cria_trecho_voo_com_tupla, trecho_voos))
