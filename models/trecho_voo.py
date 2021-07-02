class Trecho_voo:
    def __init__(self, numero_voo, codigo_aeroporto_partida, horario_partida_previsto, codigo_aeroporto_chegada, horario_chegada_previsto, numero_trecho=None):
        self.numero_voo = numero_voo
        self.numero_trecho = numero_trecho
        self.codigo_aeroporto_partida = codigo_aeroporto_partida
        self.horario_partida_previsto = horario_partida_previsto
        self.codigo_aeroporto_chegada = codigo_aeroporto_chegada
        self.horario_chegada_previsto = horario_chegada_previsto