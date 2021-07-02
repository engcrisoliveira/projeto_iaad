begin;
create database if not exists companhia_aerea;
use companhia_aerea;

create table if not exists AEROPORTO(
	Codigo_aeroporto VARCHAR(20),
    Nome VARCHAR(20),
    Cidade VARCHAR(20),
    Estado VARCHAR(20),
    PRIMARY KEY(Codigo_aeroporto));

create table if not exists VOO(
	Numero_voo VARCHAR(20),
    Companhia_aerea VARCHAR(20),
    Dias_semana VARCHAR(20),
    PRIMARY KEY(Numero_voo));
    
create table if not exists TRECHO_VOO(
	Numero_trecho INT,
    Numero_voo VARCHAR(20),
    Codigo_aeroporto_partida VARCHAR(20),
    Codigo_aeroporto_chegada VARCHAR(20),
    Horario_partida_previsto VARCHAR(20),
    Horario_aeroporto_chegada VARCHAR(20),
    PRIMARY KEY(Numero_trecho, Numero_voo),
    FOREIGN KEY (Numero_voo) REFERENCES VOO(Numero_voo));

create table if not exists TIPO_AERONAVE(
	Nome_tipo_aeronave VARCHAR(20),
    Qtd_max_assentos VARCHAR(10),
    Companhia VARCHAR(45),
    PRIMARY KEY(Nome_tipo_aeronave));

create table if not exists AERONAVE(
	Codigo_aeronave VARCHAR(5),
    Numero_total_assentos VARCHAR(10),
    Tipo_aeronave VARCHAR(20),
    PRIMARY KEY(Codigo_aeronave),
    FOREIGN KEY (Tipo_aeronave) REFERENCES TIPO_AERONAVE(Nome_tipo_aeronave));

create table if not exists INSTANCIA_TRECHO(
	Numero_voo VARCHAR(20),
    Numero_trecho INT,
    Dataa DATE,
    Numero_assentos_disponiveis VARCHAR(20),
    Codigo_aeronave VARCHAR(5),
    Codigo_aeroporto_partida VARCHAR(20),
    Horario_partida VARCHAR(20),
    Codigo_aeroporto_chegada VARCHAR(20),
    Horario_chegada VARCHAR(20),
    PRIMARY KEY(Numero_voo, Numero_trecho, Dataa),
    FOREIGN KEY(Numero_voo) REFERENCES VOO(Numero_voo),
    FOREIGN KEY(Numero_trecho) REFERENCES TRECHO_VOO(Numero_trecho),
    FOREIGN KEY(Codigo_aeronave) REFERENCES AERONAVE(Codigo_aeronave),
    FOREIGN KEY(Codigo_aeroporto_partida) REFERENCES AEROPORTO(Codigo_aeroporto),
    FOREIGN KEY(Codigo_aeroporto_chegada) REFERENCES AEROPORTO(Codigo_aeroporto));

create table if not exists RESERVA_ASSENTO(
	Numero_voo VARCHAR(6),
    Numero_trecho INT,
    Dataa DATE,
    Numero_assento VARCHAR(10),
    Nome_cliente VARCHAR(50),
    Telefone_cliente VARCHAR(10),
    PRIMARY KEY(Numero_voo, Numero_trecho, Dataa, Numero_assento),
    FOREIGN KEY(Numero_voo) REFERENCES VOO(Numero_voo),
    FOREIGN KEY(Numero_trecho) REFERENCES TRECHO_VOO(Numero_trecho));

create table if not exists TARIFA(
	Numero_voo VARCHAR(6),
    Codigo_tarifa INT,
    Quantidade INT,
    Restricoes VARCHAR(50),
    PRIMARY KEY(Codigo_tarifa),
	FOREIGN KEY(Numero_voo) REFERENCES VOO(Numero_voo));

create table if not exists PODE_POUSAR(
	Nome_tipo_aeronave VARCHAR(45),
    Codigo_aeroporto VARCHAR(5),
    PRIMARY KEY(Nome_tipo_aeronave, Codigo_aeroporto),
    FOREIGN KEY(Nome_tipo_aeronave) REFERENCES TIPO_AERONAVE(Nome_tipo_aeronave),
    FOREIGN KEY(Codigo_aeroporto) REFERENCES AEROPORTO(Codigo_aeroporto));
    

    
