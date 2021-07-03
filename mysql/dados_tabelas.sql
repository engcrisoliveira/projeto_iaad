alter table aeroporto modify Nome varchar(60);
alter table aeroporto modify Nome varchar(60);
alter table voo modify Companhia_aerea varchar(40);

select * from aeroporto;
insert into TIPO_AERONAVE values
('Boeing 737-800', '186', 'Gol Linhas Aéreas'),
('Boeing 737-700', '146', 'Gol Linhas Aéreas'),
('A319', '144', 'LATAM Airlines'),
('Airbus 319-100', '144', 'LATAM Airlines'),
('Airbus 321-200', '220', 'LATAM Airlines'),
('Airbus 320-200', '174', 'LATAM Airlines'),
('Airbus 320neo', '165', 'Azul Linhas Aéreas Brasileiras'),
('Embraer 195E2', '165', 'Azul Linhas Aéreas Brasileiras');

insert into AERONAVE(Numero_total_assentos, Tipo_aeronave) values 
(186, 'Boeing 737-800'),
(144, 'Airbus 319-100'),
(174, 'Airbus 320-200'),
(165, 'Airbus 320neo'),
(165, 'Embraer 195E2');

insert into VOO(Companhia_aerea, Dias_semana) values 
('Gol Linhas Aéreas', 'segunda-feira'),
('LATAM Airlines', 'quarta-feira'),
('LATAM Airlines', 'sexta-feira'),
('Azul Linhas Aéreas Brasileiras', 'terça-feira'),
('Azul Linhas Aéreas Brasileiras', 'segunda-feira'),
('Gol Linhas Aéreas', 'sábado');


insert into AEROPORTO(Nome, Cidade, Estado) values 
('Aeroporto Internacional de Rio Branco', 'Rio Branco', 'AC'),
('Aeroporto Internacional de Florianópolis/Hercílio Luz', 'Florianópolis', 'SC'),
('Aeroporto Internacional do Recife/ Guararapes', 'Recife', 'PE'),
('Aeroporto Internacional de Curitiba/Afonso Pena', 'Curitiba', 'PR'),
('Aeroporto Internacional de Fortaleza/Pinto Martins', 'Fortaleza', 'CE'),
('Aeroporto Internacional de Brasília', 'Brasília', 'DF'),
('Aeroporto Internacional de Natal/Augusto Severo', 'Natal', 'RN'),
('Aeroporto Internacional de João Pessoa', 'João Pessoa', 'PB'),
('Aeroporto Internacional do Rio de Janeiro', 'Galeão', 'RJ'),
('Aeroporto Internacional de São Paulo/Guarulhos','Guarulhos','SP');
 

insert into TRECHO_VOO(Numero_voo, Codigo_aeroporto_partida, Codigo_aeroporto_chegada, Horario_partida_previsto, Horario_chegada_previsto) values
(13, 11, 12, '14:00','18:07'),
(14, 16, 20, '07:00', '08:45'),
(15, 18, 19, '10:00', '13:10'),
(16, 13, 14, '22:00', '01:00'),
(17, 17, 20, '20:00', '23:30'),
(18, 15, 16, '06:00', '8:50');

INSERT INTO INSTANCIA_TRECHO values
(13, 7, '2021-08-16', 40, 11, 11, '14:00', 12, '18:07'),
(14, 8, '2021-08-18', 100,12, 16, '07:00', 20, '08:45'),
(15, 9, '2021-08-20', 80,13, 18, '10:00', 19, '13:10'),
(16, 10, '2021-08-24', 40,14, 13, '22:00', 14, '01:00'),
(17, 11, '2021-08-23', 50,15, 17, '20:00', 20, '23:30'),
(18, 12, '2021-08-28', 60,11, 15, '06:00', 16, '08:50');

insert into RESERVA_ASSENTO values
(13, 7, '2021-08-16', 161, 'Josenildo Tavares', '98952-9875'),
(14, 8, '2021-08-18', 103, 'Miranda Silva', '98426-1152'),
(15, 9, '2021-08-20', 106, 'Ravi Mendonça', '99426-6143'),
(16, 10,'2021-08-24', 005, 'Amanda Soares', '98413-2416'),
(17, 11, '2021-08-23', 059, 'Felipe Costa', '99115-5641'),
(18,12, '2021-08-28', 085, 'Fernanda Monteiro', 99841-5454);

insert into pode_pousar values 
('Boeing 737-800', 12),
('Airbus 319-100', 20),
('Airbus 320-200', 19),
('Airbus 320neo', 14),
('Embraer 195E2', 20),
('Boeing 737-800', 16);

insert into TARIFA(Numero_voo, Quantidade, Restricoes) values
(13, 4, 'Nenhuma'),
(14, 3, 'Nenhuma'),
(15, 6, 'Nenhuma'),
(16, 0, 'Nenhuma'),
(17, 1, 'Nenhuma'),
(18, 0, 'Nenhuma');
