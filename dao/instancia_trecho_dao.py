from models.instancia_trecho import Instancia_trecho

SQL_DELETA_INSTANCIA = 'delete from Instancia_Trecho where Numero_trecho = %s and Numero_voo = %s'
SQL_ATUALIZA_INSTANCIA = 'update Instancia_Trecho set Dataa = %s, Numero_assentos_disponiveis = %s, Codigo_aeronave = %s, Codigo_aeroporto_partida = %s, Horario_partida = %s, Codigo_aeroporto_chegada = %s, Horario_chegada = %s where Numero_trecho = %s and Numero_voo = %s'
SQL_INSTANCIA_POR_NUMERO_TRECHO = 'select Numero_trecho, Numero_voo, Dataa, Numero_assentos_disponiveis, Codigo_aeronave, Codigo_aeroporto_partida, Horario_partida, Codigo_aeroporto_chegada, Horario_chegada where Numero_trecho = %s and Numero_voo = %s'
SQL_BUSCA_INSTANCIA = 'select Numero_trecho, Numero_voo, Dataa, Numero_assentos_disponiveis, Codigo_aeronave, Codigo_aeroporto_partida, Horario_partida, Codigo_aeroporto_chegada, Horario_chegada from Instancia_Trecho'
SQL_CRIA_INSTANCIA = 'insert into Instancia_Trecho(Numero_trecho, Numero_voo, Dataa, Numero_assentos_disponiveis, Codigo_aeronave, Codigo_aeroporto_partida, Horario_partida, Codigo_aeroporto_chegada, Horario_chegada) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)'


class Instancia_trechodao:
    def __init__(self, db):
        self.__db = db
    
    def salvar(self, instancia_trecho):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CRIA_INSTANCIA, (instancia_trecho.numero_voo, instancia_trecho.numero_trecho, instancia_trecho.dataa, instancia_trecho.codigo_aeronave, instancia_trecho.codigo_aeroporto_partida, instancia_trecho.horario_partida, instancia_trecho.codigo_aeroporto_chegada, instancia_trecho.horario_chegada))
        self.__db.connection.commit()
        return instancia_trecho
    
    def atualizar(self, instancia_trecho, instancia_escolhida):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_ATUALIZA_INSTANCIA, (instancia_escolhida.numero_voo, instancia_escolhida.numero_trecho, instancia_trecho.dataa, instancia_trecho.codigo_aeronave, instancia_trecho.codigo_aeroporto_partida, instancia_trecho.horario_partida, instancia_trecho.codigo_aeroporto_chegada, instancia_trecho.horario_chegada))
        self.__db.connection.commit()
        return instancia_trecho
    
    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_INSTANCIA)
        instancia_trecho = traduz_instancia_trecho(cursor.fetchall())
        return instancia_trecho
    
    def buscar_instancia_pelo_numero_trecho(self, numero_voo, numero_trecho):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_INSTANCIA_POR_NUMERO_TRECHO, (numero_voo, numero_trecho))
        tupla = cursor.fetchone()
        return Instancia_trecho(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8])
    
    def deletar(self, numero_voo, numero_trecho):
        self.__db.connection.cursor().execute(SQL_DELETA_INSTANCIA, (numero_voo, numero_trecho))
        self.__db.connection.commit()
    
def traduz_instancia_trecho(instancia_trecho):
    def cria_instancia_com_tupla(tupla):
        return Instancia_trecho(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8])
    return list(map(cria_instancia_com_tupla, instancia_trecho))
