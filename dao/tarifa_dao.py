from models.tarifa import Tarifa

SQL_DELETA_TARIFA = 'delete from TARIFA where Codigo_tarifa = %s'
SQL_ATUALIZA_TARIFA = 'update TARIFA set Numero_voo = %s, Quantidade = %s, Restricoes = %s where Codigo_tarifa = %s' 
SQL_PESQUISAR_TARIFA_POR_CODIGO_TARIFA = 'select Numero_voo, Codigo_tarifa, Quantidade, Restricoes from TARIFA where Codigo_tarifa = %s'
SQL_BUSCA_TARIFA = 'select Numero_voo, Codigo_tarifa, Quantidade, Restricoes from TARIFA'
SQL_CRIA_TARIFA = 'insert into TARIFA (Numero_voo, Quantidade, Restricoes) values (%s, %s, %s)'

class TarifaDao:
    def __init__(self,db):
        self.__db = db

    def salvar(self, tarifa):
        cursor = self.__db.connection.cursor()

        if (tarifa.codigo_tarifa):
            cursor.execute(SQL_ATUALIZA_TARIFA, (tarifa.numero_voo, tarifa.quantidade, tarifa.restricoes, tarifa.codigo_tarifa))
        else:
            cursor.execute(SQL_CRIA_TARIFA, (tarifa.numero_voo, tarifa.quantidade, tarifa.restricoes))
            tarifa.codigo_tarifa = cursor.lastrowid
        self.__db.connection.commit()
        return tarifa
    
    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_TARIFA)
        tarifas = traduz_tarifas(cursor.fetchall())
        return tarifas
    
    def buscar_tarifa_por_codigo(self, Codigo_tarifa):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_PESQUISAR_TARIFA_POR_CODIGO_TARIFA, (Codigo_tarifa, ))
        tupla = cursor.fetchone()
        return Tarifa(tupla[0], tupla[2], tupla[3], codigo_tarifa = tupla[1])
    
    def deletar(self, Codigo_tarifa):
        self.__db.connection.cursor().execute(SQL_DELETA_TARIFA, (Codigo_tarifa, ))
        self.__db.connection.commit()

def traduz_tarifas(tarifas):
    def cria_tarifas_com_tupla(tupla):
        return Tarifa(tupla[0], tupla[2], tupla[3], codigo_tarifa=tupla[1])
    return list(map(cria_tarifas_com_tupla, tarifas))
