import psycopg2

conn = psycopg2.connect(host = "200.129.44.249", database = "TRABALHO_02(542561)", user = "542561" , password = "542561@fbd" )
cur = conn.cursor()

# Implementar o gatilho 1

gatilho1_sql = """
CREATE OR REPLACE FUNCTION garantir_apenas_um_capitao()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.funcao = 'Capitao' THEN
        IF EXISTS (SELECT * FROM Tripulantes WHERE Tripulantes.id_trp <> NEW.id_trp AND funcao = 'Capitao') THEN
            RAISE EXCEPTION 'Não é possivel fazer alterações na tabela, pois já existe um Capitao';
        END IF;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER garantir_apenas_um_capitao
BEFORE INSERT OR UPDATE ON Tripulantes
FOR EACH ROW
EXECUTE FUNCTION garantir_apenas_um_capitao();
"""

# Implementar o gatilho 2
gatilho2_sql = """
CREATE OR REPLACE FUNCTION restringir_empregados_manutencao()
RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (SELECT * FROM Movimentacoes WHERE NEW.id_mov = Movimentacoes.id_mov AND tipo = 'Manutencao') THEN
        IF NOT EXISTS (SELECT * FROM Empregados WHERE Empregados.id_emp = NEW.id_emp AND funcao = 'Manutencao') THEN
            RAISE EXCEPTION 'Somente empregados da manutencao podem ser escolhidos para movimentacoes do tipo Manutencao';
        END IF;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trig_restringir_empregados_manutencao
BEFORE INSERT ON Movimentacoes_Empregados
FOR EACH ROW
EXECUTE FUNCTION restringir_empregados_manutencao();
"""

# Executar scripts SQL
cur.execute(gatilho1_sql)
cur.execute(gatilho2_sql)

# Commit para aplicar as alterações no banco de dados
conn.commit()

# Tentar inserir tuplas na tabela "Movimentacoes_Empregados"
try:
    # Inserir tuplas na tabela "Movimentacoes_Empregados"
    cur.execute("INSERT INTO Movimentacoes_Empregados (id_mov, id_emp) VALUES (5, 5)")
    conn.commit()
    cur.execute("INSERT INTO Movimentacoes_Empregados (id_mov, id_emp) VALUES (5, 2)")
    conn.commit()

    # Tentar modificar o valor do atributo "funcao" do Tripulante3 para "Capitao"
    cur.execute("UPDATE Tripulantes SET funcao = 'Capitao' WHERE id_trp = 3")
    conn.commit()

except (Exception, psycopg2.Error) as error:
    print("Erro ao inserir tuplas na tabela:", error)

finally:
    if conn:
        cur.close()
        conn.close()
        print("Conexão com o PostgreSQL fechada")