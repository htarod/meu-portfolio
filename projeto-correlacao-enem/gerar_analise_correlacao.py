import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr


print("Diretório atual:", os.getcwd())


caminho_dados = os.path.join("dados", "MICRODADOS_ENEM_ESCOLA.csv")
df = pd.read_csv(caminho_dados, sep=";", encoding="latin1", low_memory=False)


colunas = ['NU_ANO', 'NO_MUNICIPIO_ESCOLA', 'NU_MATRICULAS', 'NU_MEDIA_OBJ']
df = df[colunas]
df = df.dropna()


df['NU_MATRICULAS'] = pd.to_numeric(df['NU_MATRICULAS'], errors='coerce')
df['NU_MEDIA_OBJ'] = pd.to_numeric(df['NU_MEDIA_OBJ'], errors='coerce')
df = df.dropna()


corr, pval = pearsonr(df['NU_MATRICULAS'], df['NU_MEDIA_OBJ'])
print(f"Coeficiente de correlação de Pearson: {corr:.4f}")
print(f"p-valor: {pval:.4f}")


os.makedirs("imagens", exist_ok=True)


plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="NU_MATRICULAS", y="NU_MEDIA_OBJ", alpha=0.4)
plt.title("Correlação entre Número de Matrículas e Nota Média")
plt.xlabel("Número de Matrículas")
plt.ylabel("Nota Média")
plt.savefig("imagens/dispersao-matriculas-vs-nota.png")
plt.close()


df_corr = df.select_dtypes(include="number").corr()

plt.figure(figsize=(10, 8))
sns.heatmap(df_corr, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Matriz de Correlação")
plt.savefig("imagens/matriz-correlacao.png")
plt.close()


correlacoes = df_corr.unstack().sort_values(ascending=False).drop_duplicates()
top10 = correlacoes[correlacoes.index.get_level_values(0) != correlacoes.index.get_level_values(1)].abs().nlargest(10)
top10_df = pd.DataFrame(top10).reset_index()
top10_df.columns = ['Variável 1', 'Variável 2', 'Correlação']

pivot = top10_df.pivot(index='Variável 1', columns='Variável 2', values='Correlação')
plt.figure(figsize=(8, 6))
sns.heatmap(pivot, annot=True, cmap='Blues')
plt.title("Top 10 Correlações Absolutas")
plt.savefig("imagens/heatmap-top-correlacoes.png")
plt.close()
