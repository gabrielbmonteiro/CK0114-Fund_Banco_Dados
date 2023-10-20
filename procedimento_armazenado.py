import psycopg2

conn = psycopg2.connect(host = "200.129.44.249", database = "TRABALHO_02(542561)", user = "542561" , password = "542561@fbd" )
cur = conn.cursor()

# Cria o Procedimento Armazenado:

#1. Crie um procedimento armazenado no banco de dados com nome empregado_do_mes que recebe como parâmetro uma data e retorna o 
#   id e nome do empregado que participou de mais movimentações naquela combinação Ano/Mês;
cur.execute("CREATE OR REPLACE FUNCTION empregado_do_mes(data_param DATE) "
            "RETURNS TABLE (id_emp INT, nome_emp VARCHAR) AS "
            "$$ "
            "DECLARE "
            "   max_mov_count INT; "
            "BEGIN "
            "    SELECT MAX(mov_count) "
            "    INTO max_mov_count "
            "    FROM ( "
            "        SELECT COUNT(*) AS mov_count "
            "        FROM Movimentacoes_Empregados ME "
            "        JOIN Movimentacoes M ON ME.id_mov = M.id_mov "
            "        WHERE EXTRACT(YEAR FROM M.data) = EXTRACT(YEAR FROM data_param) "
            "        AND EXTRACT(MONTH FROM M.data) = EXTRACT(MONTH FROM data_param) "
            "        GROUP BY ME.id_emp "
            "    ) AS counts; "
            "    RETURN QUERY "
            "    SELECT ME.id_emp, E.nome "
            "    FROM Movimentacoes_Empregados ME "
            "    JOIN Empregados E ON ME.id_emp = E.id_emp "
            "    JOIN Movimentacoes M ON ME.id_mov = M.id_mov "
            "    WHERE EXTRACT(YEAR FROM M.data) = EXTRACT(YEAR FROM data_param) "
            "    AND EXTRACT(MONTH FROM M.data) = EXTRACT(MONTH FROM data_param) "
            "    GROUP BY ME.id_emp, E.nome "
            "    HAVING COUNT(*) = max_mov_count; "
            "END; "
            "$$ LANGUAGE plpgsql; " 
            )

conn.commit()

#2. Escreve um novo script Python que chama o procedimento armazenado criado no item anterior passando como parâmetro a data 2023-10-01
try:
    #chama o procedimento armazenado 
    cur.execute("SELECT empregado_do_mes ('2023-10-01');")

    # Recuperar os resultados
    results = cur.fetchall()

    # Imprimir os resultados (ou fazer o que desejar com eles)
    for result in results:
        print(result)

    #Fecha a comunicação com o banco de dados 
    cur.close()

except (Exception, psycopg2.DatabaseError) as error: 
    print (error)
finally:
    if conn is not None: 
        conn.close()