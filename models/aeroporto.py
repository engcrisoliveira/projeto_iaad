class Aeroporto:
    def __init__(self, nome, cidade, estado, codigo_aeroporto=None):
        self.codigo_aeroporto = codigo_aeroporto
        self.nome = nome
        self.cidade = cidade
        self.estado = estado