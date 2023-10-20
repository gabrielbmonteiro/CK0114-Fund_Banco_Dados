import psycopg2

conn = psycopg2.connect(host = "200.129.44.249", database = "TRABALHO_02(542561)", user = "542561" , password = "542561@fbd" )
cur = conn.cursor()

# Faz Consultas na Tabela:

#1. Retorne todas as embarcações e o número de tripulantes de cada embarcação.
cur.execute("SELECT e.id_emb, e.nome, e.tipo, COUNT(t.id_trp) AS numero_tripulantes "
            "FROM Embarcacoes e "
            "LEFT JOIN Tripulantes t ON e.id_emb = t.id_emb "
            "GROUP BY e.id_emb ")

result1 = cur.fetchall()
print("Consulta 1 - Embarcações e Número de tripulantes ")
for row in result1:
    print(f"ID: {row[0]}, Nome: {row[1]}, Tipo: {row[2]}, Número de Tripulantes: {row[3]}")


#2. Retorne os Empregados envolvidos na movimentação de ID 1.
cur.execute("SELECT emp.nome, emp.data_nasc, emp.funcao "
            "FROM Empregados emp, Movimentacoes_Empregados me "
            "WHERE me.id_mov = 1 and me.id_emp = emp.id_emp; ")

result2 = cur.fetchall()
print("\nConsulta 2 - Empregados envolvidos na movimentação de ID 1")
for row in result2:
    print(f"Empregado: {row[0]}, Data de Nascimento: {row[1]}, Função: {row[2]}")

#3. Retorne a quantidade de movimentações que envolvem embarcações do tipo “Cargueiro”.
cur.execute("SELECT COUNT(mov.id_mov) AS quantidade_movimentacoes_cargueiro "
            "FROM Movimentacoes mov "
            "INNER JOIN Embarcacoes emb ON mov.id_emb = emb.id_emb "
            "WHERE emb.tipo = 'Cargueiro'; ")

result3 = cur.fetchall()
print("\nConsulta 3 - Quantidade de movimentações envolvendo embarcações do tipo 'Cargueiro'")
for row in result3:
    print(f"Quantidade de Movimentações: {row[0]}")

# Feche o cursor e a conexão
cur.close()
conn.close()