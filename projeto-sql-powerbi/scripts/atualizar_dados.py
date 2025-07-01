
import sqlite3
import pandas as pd
import os

caminho_csv = os.path.join('dados', 'bcdata.sgs.433.csv')
caminho_banco = os.path.join('banco', 'indicadores.db')

df = pd.read_csv(caminho_csv, sep=';', decimal=',')
df.columns = ['data', 'valor']

df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

con = sqlite3.connect(caminho_banco)
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS ipca;")
cur.execute("""
    CREATE TABLE ipca (
        data TEXT PRIMARY KEY,
        valor REAL
    );
""")

df.to_sql('ipca', con, if_exists='append', index=False)

con.commit()
con.close()

print("Dados atualizados com sucesso.")
