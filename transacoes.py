import psycopg2

conn = psycopg2.connect(host = "200.129.44.249", database = "TRABALHO_02(542561)", user = "542561" , password = "542561@fbd" )

# Faz Transações:

try:
    cur = conn.cursor()

    # 1. Inserir nova Movimentação: (6, ‘2023-10-05’, ‘Movimentação’, 1)
    cur.execute("INSERT INTO Movimentacoes (id_mov, data, tipo, id_emb) VALUES (%s, %s, %s, %s)", (6, '2023-10-05', 'Manutencao', 1))

    # Commit para confirmar a primeira operação
    conn.commit()

    # 2. Inserir nova Movimentação_Empregado: (6, 1)
    cur.execute("INSERT INTO Movimentacoes_Empregados (id_mov, id_emp) VALUES (%s, %s)", (6, 1))

    # Commit para confirmar as operações na transação
    conn.commit()

    # 3. Retornar a quantidade de movimentações que envolvem embarcações do tipo “Cargueiro”
    cur.execute("SELECT COUNT(mov.id_mov) AS quantidade_movimentacoes "
                "FROM Movimentacoes mov "
                "INNER JOIN Embarcacoes emb ON mov.id_emb = emb.id_emb "
                "WHERE emb.tipo = 'Cargueiro'; ")
          
    quantidade_movimentacoes_cargueiro = cur.fetchall()
    for row in quantidade_movimentacoes_cargueiro:
        print(f"Quantidade de Movimentações: {row[0]}")

    cur.close()

except psycopg2.DatabaseError as error:
    print(error)

finally:
    if conn is not None:
        conn.close()