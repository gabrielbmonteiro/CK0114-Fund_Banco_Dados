# CK0114 - Fundamentos de Banco de Dados 🗄️

Este repositório contém o ecossistema de banco de dados desenvolvido como projeto prático para a disciplina de **Fundamentos de Banco de Dados (FBD)**. O objetivo principal é demonstrar a integração de uma camada de aplicação escrita em **Python** com um Sistema Gerenciador de Banco de Dados Relacional (SGBD), cobrindo desde a modelagem física até a automação de regras de negócio e controle transacional.

## 🚀 Arquitetura e Módulos do Projeto

O projeto foi modularizado para refletir com fidelidade o ciclo de vida e as boas práticas de administração de um banco de dados relacional:

* **`cria_tabela.py` (Camada DDL):** Contém os scripts de definição de dados. Responsável por mapear o modelo relacional criando as tabelas, definindo os tipos de dados e aplicando restrições de integridade rígidas, como Chaves Primárias (`PRIMARY KEY`), Chaves Estrangeiras (`FOREIGN KEY`) e restrições de unicidade.
* **`insere_dados.py` (Camada DML):** Script focado na manipulação e população inicial do ambiente. Insere registros simulados de forma consistente para que os testes e queries tenham uma base de dados realista para operar.
* **`consultas.py` (Queries & Álgebra Relacional):** Centraliza as buscas e relatórios do sistema. Implementa consultas SQL complexas utilizando junções múltiplas (`INNER/LEFT JOIN`), funções de agregação (`COUNT`, `SUM`, `AVG`), filtros agrupados (`GROUP BY` / `HAVING`) e subconsultas estruturadas.
* **`gatilhos.py` (Triggers):** Implementa gatilhos automáticos disparados diretamente no banco de dados antes ou depois de eventos de escrita (`INSERT`, `UPDATE`, `DELETE`). Ideal para auditoria e aplicação automática de regras de negócio.
* **`procedimento_armazenado.py` (Stored Procedures):** Rotinas otimizadas e encapsuladas diretamente no SGBD para processamento de regras complexas do lado do servidor, reduzindo o tráfego de rede e isolando a lógica de dados.
* **`transacoes.py` (Controle ACID):** Demonstra o gerenciamento manual de transações lógicas no banco de dados. Utiliza os comandos de controle de concorrência e integridade (`COMMIT` e `ROLLBACK`) para garantir propriedades ACID (Atomicidade, Consistência, Isolamento e Durabilidade).

## 🛠️ Tecnologias Utilizadas

* **Linguagem Core:** Python 3
* **Paradigma:** Banco de Dados Relacional (SQL)
* **Drivers de Conexão:** Integração nativa Python-SGBD

## 🔧 Ordem Lógica de Execução

Para rodar e testar o ambiente localmente no terminal, os scripts devem seguir a ordem de dependência das tabelas:

1. Gere a estrutura física do banco de dados:
   ```bash
   python cria_tabela.py
2. Popule o banco com os dados iniciais:
   ```bash
   python insere_dados.py
3. Execute os módulos de consultas, automações e segurança transacional:
   ```bash
   python consultas.py
   python gatilhos.py
   python transacoes.py
