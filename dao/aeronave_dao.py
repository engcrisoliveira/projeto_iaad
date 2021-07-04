from models.aeronave import Aeronave

SQL_DELETA_AERONAVE = 'delete from aeronave where Codigo_aeronave = %s'
SQL_AERONAVE_POR_CODIGO_AERONAVE = 'SELECT Codigo_aeronave, numero_total_assentos, tipo_aeronave from aeronave where Codigo_aeronave = %s'
SQL_ATUALIZA_AERONAVE = 'UPDATE aeronave SET numero_total_assentos=%s, tipo_aeronave=%s where Codigo_aeronave = %s'
SQL_BUSCA_AERONAVES = 'SELECT Codigo_aeronave, numero_total_assentos, tipo_aeronave from aeronave'
SQL_CRIA_AERONAVE = 'INSERT into aeronave (numero_total_assentos, tipo_aeronave) values (%s, %s)'

class AeronaveDao:
    def __init__(self,db):
        self.__db = db
    
    def salvar(self,aeronave):
        cursor = self.__db.connection.cursor()

        if (aeronave.codigo_aeronave):
            cursor.execute(SQL_ATUALIZA_AERONAVE,(aeronave.numero_total_assentos, aeronave.tipo_aeronave))
        else:
            cursor.execute(SQL_CRIA_AERONAVE, (aeronave.numero_total_assentos, aeronave.tipo_aeronave))
            aeronave.codigo_aeronave = cursor.lastrowid
        self.__db.connection.commit()
        return aeronave

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_AERONAVES)
        aeronaves = traduz_aeronaves(cursor.fetchall())
        return aeronaves

    def busca_por_codigo_aeronave(self, codigo_aeronave):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_AERONAVE_POR_CODIGO_AERONAVE, (codigo_aeronave))
        tupla = cursor.fetchone()
        return Aeronave(tupla[1],tupla[2], codigo_aeronave=tupla[0])

    def deletar(self, codigo_aeronave):
        self.__db.connection.cursor().execute(SQL_DELETA_AERONAVE, (codigo_aeronave))
        self.__db.connection.commit()

def traduz_aeronaves(aeronaves):
    def cria_aeronave_com_tupla(tupla):
        return Aeronave(tupla[1], tupla[2], codigo_aeronave=tupla[0])
    return list(map(cria_aeronave_com_tupla, aeronaves))
