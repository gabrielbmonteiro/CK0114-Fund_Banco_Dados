import psycopg2

conn = psycopg2.connect(host = "200.129.44.249", database = "TRABALHO_02(542561)", user = "542561" , password = "542561@fbd" )
cur = conn.cursor()

# Faz a Inserção de Dados:

# Tabela Embarcacoes
cur.execute("INSERT INTO Embarcacoes(nome, tipo) VALUES (%s, %s)", ('Navio1', 'Cargueiro'))
cur.execute("INSERT INTO Embarcacoes(nome, tipo) VALUES (%s, %s)", ('Navio2', 'Passageiro'))
cur.execute("INSERT INTO Embarcacoes(nome, tipo) VALUES (%s, %s)", ('Navio3', 'Petroleiro'))
cur.execute("INSERT INTO Embarcacoes(nome, tipo) VALUES (%s, %s)", ('Navio4', 'Cargueiro'))

# Tabela Tripulantes
cur.execute("INSERT INTO Tripulantes(nome, data_nasc, funcao, id_emb) VALUES (%s, %s, %s, %s)", ('Tripulante1', '1990-01-15','Oficial de Conves', 1))
cur.execute("INSERT INTO Tripulantes(nome, data_nasc, funcao, id_emb) VALUES (%s, %s, %s, %s)", ('Tripulante2', '1992-03-20','Engenheiro', 1))
cur.execute("INSERT INTO Tripulantes(nome, data_nasc, funcao, id_emb) VALUES (%s, %s, %s, %s)", ('Tripulante3', '1988-11-05','Comissario de Bordo', 2))
cur.execute("INSERT INTO Tripulantes(nome, data_nasc, funcao, id_emb) VALUES (%s, %s, %s, %s)", ('Tripulante4', '1995-06-30','Oficial de Conves', 3))
cur.execute("INSERT INTO Tripulantes(nome, data_nasc, funcao, id_emb) VALUES (%s, %s, %s, %s)", ('Tripulante5', '1991-07-10','Capitao', 4))
cur.execute("INSERT INTO Tripulantes(nome, data_nasc, funcao, id_emb) VALUES (%s, %s, %s, %s)", ('Tripulante6', '1994-09-25','Engenheiro', 4))

# Tabela Empregados
cur.execute("INSERT INTO Empregados(nome, data_nasc, funcao) VALUES (%s, %s, %s)", ('Employee1', '1985-05-12', 'Manutencao'))
cur.execute("INSERT INTO Empregados(nome, data_nasc, funcao) VALUES (%s, %s, %s)", ('Employee2', '1993-02-28', 'Seguranca'))
cur.execute("INSERT INTO Empregados(nome, data_nasc, funcao) VALUES (%s, %s, %s)", ('Employee3', '1987-09-18', 'Logistica'))
cur.execute("INSERT INTO Empregados(nome, data_nasc, funcao) VALUES (%s, %s, %s)", ('Employee4', '1990-12-05', 'Limpeza'))
cur.execute("INSERT INTO Empregados(nome, data_nasc, funcao) VALUES (%s, %s, %s)", ('Employee5', '2001-08-30', 'Manutencao'))

# Tabela Movimentacoes
cur.execute("INSERT INTO Movimentacoes(data, tipo, id_emb) VALUES (%s, %s, %s)", ('2023-09-01', 'Carga', 1))
cur.execute("INSERT INTO Movimentacoes(data, tipo, id_emb) VALUES (%s, %s, %s)", ('2023-09-02', 'Embarque de Passageiros', 2))
cur.execute("INSERT INTO Movimentacoes(data, tipo, id_emb) VALUES (%s, %s, %s)", ('2023-10-03', 'Abastecimento', 3))
cur.execute("INSERT INTO Movimentacoes(data, tipo, id_emb) VALUES (%s, %s, %s)", ('2023-10-05', 'Descarga', 1))
cur.execute("INSERT INTO Movimentacoes(data, tipo, id_emb) VALUES (%s, %s, %s)", ('2023-10-05', 'Manutencao', 4))

# Tabela Movimentacoes_Empregados
cur.execute("INSERT INTO Movimentacoes_Empregados(id_mov, id_emp) VALUES (%s, %s)", (1, 1))
cur.execute("INSERT INTO Movimentacoes_Empregados(id_mov, id_emp) VALUES (%s, %s)", (1, 3))
cur.execute("INSERT INTO Movimentacoes_Empregados(id_mov, id_emp) VALUES (%s, %s)", (2, 2))
cur.execute("INSERT INTO Movimentacoes_Empregados(id_mov, id_emp) VALUES (%s, %s)", (3, 1))
cur.execute("INSERT INTO Movimentacoes_Empregados(id_mov, id_emp) VALUES (%s, %s)", (3, 4))
cur.execute("INSERT INTO Movimentacoes_Empregados(id_mov, id_emp) VALUES (%s, %s)", (4, 1))
cur.execute("INSERT INTO Movimentacoes_Empregados(id_mov, id_emp) VALUES (%s, %s)", (4, 3))
cur.execute("INSERT INTO Movimentacoes_Empregados(id_mov, id_emp) VALUES (%s, %s)", (5, 1))


# Commit para salvar as alterações no banco de dados
conn.commit()

# Feche o cursor e a conexão
cur.close()
conn.close()
