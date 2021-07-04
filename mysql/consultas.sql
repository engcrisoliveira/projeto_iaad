SELECT Numero_voo, Companhia_aerea, Horario_partida_previsto, Horario_chegada_previsto FROM VOO NATURAL JOIN TRECHO_VOO;
SELECT Companhia_aerea, COUNT(*) AS total_voos FROM VOO GROUP BY Companhia_aerea;
SELECT Companhia, COUNT(*) AS Total_Aeronaves FROM TIPO_AERONAVE GROUP BY Companhia;