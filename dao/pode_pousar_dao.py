from models.pode_pousar import Pode_pousar

SQL_DELETA_PODE_POUSAR = 'delete from PODE_POUSAR where Nome_tipo_aeronave = %s and Codigo_aeroporto = %s'
SQL_ATUALIZA_PODE_POUSAR = 'UPDATE PODE_POUSAR SET Nome_tipo_aeronave = %s, Codigo_aeroporto = %s where Nome_tipo_aeronave = %s and Codigo_aeroporto = %s'
SQL_PODE_POUSAR_POR_NOME_TIPO_AERONAVE_POR_CODIGO_AEROPORTO = 'SELECT Nome_tipo_aeronave, Codigo_aeroporto from PODE_POUSAR where Nome_tipo_aeronave = %s and Codigo_aeroporto = %s'
SQL_BUSCA_PODE_POUSAR = 'SELECT Nome_tipo_aeronave, Codigo_aeroporto from PODE_POUSAR'
SQL_CRIA_PODE_POUSAR = 'INSERT into PODE_POUSAR (Nome_tipo_aeronave, Codigo_aeroporto) values (%s, %s)'


class Pode_pousarDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, pode_pousar):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CRIA_PODE_POUSAR, (pode_pousar.nome_tipo_aeronave, pode_pousar.codigo_aeroporto))
        self.__db.connection.commit()
        return pode_pousar
    
    def atualizar(self, pode_pousar, pode_pousar_escolhido):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_ATUALIZA_PODE_POUSAR, (pode_pousar.nome_tipo_aeronave, pode_pousar.codigo_aeroporto, pode_pousar_escolhido.nome_tipo_aeronave, pode_pousar_escolhido.codigo_aeroporto))
        self.__db.connection.commit()
        return pode_pousar

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_PODE_POUSAR)
        pode_pousar = traduz_pode_pousar(cursor.fetchall())
        return pode_pousar

    def busca_por_nome_tipo_aeronave_por_codigo_aeroporto(self, nome_tipo_aeronave, codigo_aeroporto):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_PODE_POUSAR_POR_NOME_TIPO_AERONAVE_POR_CODIGO_AEROPORTO, (nome_tipo_aeronave,codigo_aeroporto))
        tupla = cursor.fetchone()
        return Pode_pousar(tupla[0], tupla[1])

    def deletar(self, nome_tipo_aeronave, codigo_aeroporto):
        self.__db.connection.cursor().execute(SQL_DELETA_PODE_POUSAR, (nome_tipo_aeronave, codigo_aeroporto ))
        self.__db.connection.commit()

def traduz_pode_pousar(pode_pousar):
    def cria_pode_pousar_com_tupla(tupla):
        return Pode_pousar(tupla[0], tupla[1])
    return list(map(cria_pode_pousar_com_tupla, pode_pousar))
