from models.reserva_assento import Reserva_assento

SQL_DELETA_RESERVA_ASSENTO = 'delete from Reserva_assento where Numero_voo = %s and Numero_trecho=%s and Dataa=%s and Numero_assento = %s'
SQL_RESERVA_ASSENTO_POR_NUMERO_ASSENTO = 'SELECT Numero_voo, Numero_trecho, Dataa, Numero_assento, Nome_cliente, Telefone_cliente from Reserva_assento where Numero_voo = %s and Numero_trecho=%s and Dataa=%s and Numero_assento = %s'
SQL_ATUALIZA_RESERVA_ASSENTO = 'UPDATE Reserva_assento SET Numero_voo=%s, Numero_trecho=%s, Dataa=%s, Numero_assento= %s, Nome_cliente=%s, Telefone_cliente=%s where Numero_voo = %s and Numero_trecho=%s and Dataa=%s and Numero_assento = %s'
SQL_BUSCA_RESERVAS_ASSENTO = 'SELECT Numero_voo, Numero_trecho, Dataa, Numero_assento, Nome_cliente, Telefone_cliente from Reserva_assento'
SQL_CRIA_RESERVA_ASSENTO = 'INSERT into Reserva_assento (Numero_voo, Numero_trecho, Dataa, Numero_assento, Nome_cliente, Telefone_cliente) values (%s, %s, %s, %s, %s, %s)'

class Reserva_assentoDao:
    def __init__(self, db):
        self.__db = db
    def salvar(self, reserva_assento, reserva_assento_escolhido=None):
        cursor = self.__db.connection.cursor()
        if(reserva_assento_escolhido):
            cursor.execute(SQL_ATUALIZA_RESERVA_ASSENTO, (reserva_assento.numero_voo, 
            reserva_assento.numero_trecho, 
            reserva_assento.dataa,
            reserva_assento.numero_assento, 
            reserva_assento.nome_cliente, 
            reserva_assento.telefone_cliente,
            reserva_assento_escolhido.numero_voo,
            reserva_assento_escolhido.numero_trecho,
            reserva_assento_escolhido.dataa,
            reserva_assento_escolhido.numero_assento
            ))
        else:
            cursor.execute(SQL_CRIA_RESERVA_ASSENTO, (reserva_assento.numero_voo,
            reserva_assento.numero_trecho,
            reserva_assento.dataa,
            reserva_assento.numero_assento,
            reserva_assento.nome_cliente,
            reserva_assento.telefone_cliente))
        self.__db.connection.commit()
        return Reserva_assento
    
    def listar(self): 
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_RESERVAS_ASSENTO)
        reservas = traduz_reservas(cursor.fetchall())
        return reservas

    def buscar_reserva(self,numero_voo,numero_trecho,dataa, numero_assento):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_RESERVA_ASSENTO_POR_NUMERO_ASSENTO,(numero_voo,numero_trecho,dataa,numero_assento))
        tupla = cursor.fetchone()
        return Reserva_assento(Numero_voo = tupla[0],
            Numero_trecho = tupla[1],
            Dataa= tupla[2],
            Numero_assento = tupla[3],
            Nome_cliente = tupla[4],
            Telefone_cliente = tupla[5]
            )
    
    def deletar(self, numero_voo,numero_trecho,dataa, numero_assento):
        self.__db.connection.cursor().execute(SQL_DELETA_RESERVA_ASSENTO, (numero_voo, numero_trecho,dataa,numero_assento))
        self.__db.connection.commit()

def traduz_reservas(reservas):
    def cria_reservas_com_tupla(tupla):
        return Reserva_assento(
            tupla[0],
            tupla[1],
            tupla[2],
            tupla[3],
            tupla[4],
            tupla[5]
            )
    return list(map(cria_reservas_com_tupla, reservas))