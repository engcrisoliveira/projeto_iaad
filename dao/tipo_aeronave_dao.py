from models.tipo_aeronave import Tipo_aeronave

SQL_DELETA_TIPO_AERONAVE = 'delete from TIPO_AERONAVE where Nome_tipo_aeronave = %s'
SQL_TIPO_AERONAVE_POR_NOME_TIPO_AERONAVE = 'SELECT Nome_tipo_aeronave, Qtd_max_assentos, Companhia from TIPO_AERONAVE where Nome_tipo_aeronave = %s'
SQL_ATUALIZA_TIPO_AERONAVE = 'UPDATE TIPO_AERONAVE SET Qtd_max_assentos=%s, Companhia=%s where Nome_tipo_aeronave = %s'
SQL_BUSCA_TIPO_AERONAVES = 'SELECT Nome_tipo_aeronave, Qtd_max_assentos, Companhia from TIPO_AERONAVE'
SQL_CRIA_TIPO_AERONAVE = 'INSERT into TIPO_AERONAVE (Nome_tipo_aeronave, Qtd_max_assentos, Companhia) values (%s, %s, %s)'


class Tipo_aeronaveDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, tipo_aeronave):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CRIA_TIPO_AERONAVE, (tipo_aeronave.nome_tipo_aeronave, tipo_aeronave.qtd_max_assentos, tipo_aeronave.companhia))
        self.__db.connection.commit()
        return tipo_aeronave

    def atualizar(self, tipo_aeronave):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_ATUALIZA_TIPO_AERONAVE, (tipo_aeronave.qtd_max_assentos, tipo_aeronave.companhia, tipo_aeronave.nome_tipo_aeronave))
        self.__db.connection.commit()
        return tipo_aeronave

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_TIPO_AERONAVES)
        tipo_aeronaves = traduz_tipo_aeronaves(cursor.fetchall())
        return tipo_aeronaves

    def busca_por_nome_tipo_aeronave(self, nome_tipo_aeronave):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_TIPO_AERONAVE_POR_NOME_TIPO_AERONAVE, (nome_tipo_aeronave,))
        tupla = cursor.fetchone()
        return Tipo_aeronave(tupla[0], tupla[1], tupla[2])

    def deletar(self, nome_tipo_aeronave):
        self.__db.connection.cursor().execute(SQL_DELETA_TIPO_AERONAVE, (nome_tipo_aeronave, ))
        self.__db.connection.commit()

def traduz_tipo_aeronaves(tipo_aeronaves):
    def cria_tipo_aeronave_com_tupla(tupla):
        return Tipo_aeronave(tupla[0], tupla[1], tupla[2])
    return list(map(cria_tipo_aeronave_com_tupla, tipo_aeronaves))
