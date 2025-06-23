import pandas as pd
import sqlite3

DB_FILE = 'meu_projeto.db'

conn = sqlite3.connect(DB_FILE)

dados_completos_df = pd.read_csv('dados.csv', dtype=str)

dados_completos_df.to_sql('tabela_dados_originais', conn, if_exists='replace', index=False)

print(f"Dados de 'dados.csv' carregados para a tabela 'tabela_dados_originais' em '{DB_FILE}'")

consulta_sql = """
SELECT
    ID_Registro,
    NomeCliente,
    BAIRRO,
    TipoServico,
    Valor,
    Status,
    DataContratacao
FROM
    tabela_dados_originais
"""

resultado_df = pd.read_sql(consulta_sql, conn)

resultado_df.to_excel("dados_processados_sqlite.xlsx", index=False)

print(f"Dados importantes selecionados do SQLite e salvos em 'dados_processados_sqlite.xlsx'")
print("\nPrévia do resultado:")
print(resultado_df.head())

conn.close()
print(f"Conexão com '{DB_FILE}' fechada.")