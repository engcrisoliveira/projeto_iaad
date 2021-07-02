from models.aeroporto import Aeroporto

SQL_DELETA_AEROPORTO = 'delete from aeroporto where Codigo_aeroporto = %s'
SQL_AEROPORTO_POR_CODIGO_AEROPORTO = 'SELECT Codigo_aeroporto, nome, cidade, estado from aeroporto where Codigo_aeroporto = %s'
SQL_ATUALIZA_AEROPORTO = 'UPDATE aeroporto SET nome=%s, cidade=%s, estado=%s where Codigo_aeroporto = %s'
SQL_BUSCA_AEROPORTOS = 'SELECT Codigo_aeroporto, nome, cidade, estado from aeroporto'
SQL_CRIA_AEROPORTO = 'INSERT into aeroporto (nome, cidade, estado) values (%s, %s, %s)'


class AeroportoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, aeroporto):
        cursor = self.__db.connection.cursor()

        if (aeroporto.codigo_aeroporto):
            cursor.execute(SQL_ATUALIZA_AEROPORTO, (aeroporto.nome, aeroporto.cidade, aeroporto.estado, aeroporto.codigo_aeroporto))
        else:
            cursor.execute(SQL_CRIA_AEROPORTO, (aeroporto.nome, aeroporto.cidade, aeroporto.estado))
            aeroporto.codigo_aeroporto = cursor.lastrowid
        self.__db.connection.commit()
        return aeroporto

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_AEROPORTOS)
        aeroportos = traduz_aeroportos(cursor.fetchall())
        return aeroportos

    def busca_por_codigo_aeroporto(self, codigo_aeroporto):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_AEROPORTO_POR_CODIGO_AEROPORTO, (codigo_aeroporto,))
        tupla = cursor.fetchone()
        return Aeroporto(tupla[1], tupla[2], tupla[3], codigo_aeroporto=tupla[0])

    def deletar(self, codigo_aeroporto):
        self.__db.connection.cursor().execute(SQL_DELETA_AEROPORTO, (codigo_aeroporto, ))
        self.__db.connection.commit()

def traduz_aeroportos(aeroportos):
    def cria_aeroporto_com_tupla(tupla):
        return Aeroporto(tupla[1], tupla[2], tupla[3], codigo_aeroporto=tupla[0])
    return list(map(cria_aeroporto_com_tupla, aeroportos))
