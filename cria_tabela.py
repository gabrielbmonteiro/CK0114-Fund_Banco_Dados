import psycopg2

conn = psycopg2.connect(host = "200.129.44.249", database = "TRABALHO_02(542561)", user = "542561" , password = "542561@fbd" )
cur = conn.cursor()

# Faz a Criação de Tabelas:

# Tabela Embarcações

cur.execute("CREATE TABLE Embarcacoes ( "
            "id_emb SERIAL PRIMARY KEY, "
            "nome varchar(100) not null, "
            "tipo varchar(100) not null); "
            )

# Tabela Tripulantes
cur.execute("CREATE TABLE Tripulantes ( "
            "id_trp SERIAL PRIMARY KEY, "
            "nome varchar(100) not null, "
            "data_nasc date not null, "
            "funcao varchar(100) not null,"
            "id_emb int not null, "
            "foreign key(id_emb) references Embarcacoes); "
            )

# Tabela Empregados
cur.execute("CREATE TABLE Empregados ( "
            "id_emp SERIAL PRIMARY KEY, "
            "nome varchar(100) not null, "
            "data_nasc date not null, "
            "funcao varchar(100) not null); "
            )

# Tabela Movimentações
cur.execute("CREATE TABLE Movimentacoes ( "
            "id_mov SERIAL PRIMARY KEY, "
            "data date not null, "
            "tipo varchar(100) not null, "
            "id_emb int not null, "
            "foreign key(id_emb) references Embarcacoes); "
            )

# Tabela Movimentações_Empregados
cur.execute("CREATE TABLE Movimentacoes_Empregados ( "
            "id_mov int not null, "
            "id_emp int not null, "
            "primary key(id_mov, id_emp), "
            "foreign key(id_mov) references Movimentacoes, "
            "foreign key(id_emp) references Empregados); "
            )

# Resetar as sequências para começar em 1
cur.execute("SELECT setval(pg_get_serial_sequence('Embarcacoes', 'id_emb'), 1, false);")
cur.execute("SELECT setval(pg_get_serial_sequence('Tripulantes', 'id_trp'), 1, false);")
cur.execute("SELECT setval(pg_get_serial_sequence('Empregados', 'id_emp'), 1, false);")
cur.execute("SELECT setval(pg_get_serial_sequence('Movimentacoes', 'id_mov'), 1, false);")


# Commit para salvar as alterações no banco de dados
conn.commit()

# Feche o cursor e a conexão
cur.close()
conn.close()