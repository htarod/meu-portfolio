import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")
plt.rcParams.update({'figure.autolayout': True})

caminho_dados = "dados/Cities_Brazil_IBGE.xlsx"
caminho_imagens = "imagens"

os.makedirs(caminho_imagens, exist_ok=True)

df = pd.read_excel(caminho_dados)

colunas_float = ['IDHM', 'Pib_2014']
for col in colunas_float:
    df[col] = df[col].str.replace(',', '.').astype(float)

df['Latitude'] = df['Latitude'].astype(str).str.replace(',', '.').astype(float)
df['Longitude'] = df['Longitude'].astype(str).str.replace(',', '.').astype(float)

plt.figure(figsize=(10, 6))
sns.boxplot(x='RegiaoBrasil', y='IDHM', data=df)
plt.title('Distribuição do IDHM por Região do Brasil')
plt.xlabel('Região')
plt.ylabel('IDHM')
plt.savefig(f"{caminho_imagens}/boxplot_idhm_por_regiao.png")
plt.close()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Pib_2014', y='IDHM', hue='RegiaoBrasil', data=df, alpha=0.7)
plt.title('Relação entre PIB (2014) e IDHM')
plt.xlabel('PIB (R$ mil)')
plt.ylabel('IDHM')
plt.legend(title='Região')
plt.savefig(f"{caminho_imagens}/dispersao_pib_idhm.png")
plt.close()

df_top_idhm = df.sort_values(by='IDHM', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x='IDHM', y='LocalCidade', data=df_top_idhm, palette='viridis')
plt.title('Top 10 Cidades com Maior IDHM')
plt.xlabel('IDHM')
plt.ylabel('Cidade')
plt.savefig(f"{caminho_imagens}/top10_idhm.png")
plt.close()

df_top_pib = df.sort_values(by='Pib_2014', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x='Pib_2014', y='LocalCidade', data=df_top_pib, palette='magma')
plt.title('Top 10 Cidades com Maior PIB (2014)')
plt.xlabel('PIB (R$ mil)')
plt.ylabel('Cidade')
plt.savefig(f"{caminho_imagens}/top10_pib.png")
plt.close()

print("Imagens geradas com sucesso na pasta 'imagens'.")
