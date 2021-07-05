class Tarifa:
    def __init__(self, numero_voo, quantidade, restricoes, codigo_tarifa=None):
        self.numero_voo = numero_voo
        self.codigo_tarifa = codigo_tarifa
        self.quantidade = quantidade
        self.restricoes = restricoes