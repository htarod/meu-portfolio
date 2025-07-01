import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")
plt.rcParams.update({'figure.autolayout': True})

caminho_dados = "dados/MICRODADOS_ENEM_ESCOLA.csv"
caminho_imagens = "imagens"
os.makedirs(caminho_imagens, exist_ok=True)

colunas = ['NU_MEDIA_MT', 'NU_MEDIA_LP', 'NU_MEDIA_CH', 'TP_DEPENDENCIA_ADM_ESCOLA']
df = pd.read_csv(caminho_dados, sep=';', usecols=colunas, encoding='latin1')

df = df.dropna()

df['MEDIA_MEDIA'] = df[['NU_MEDIA_MT', 'NU_MEDIA_LP', 'NU_MEDIA_CH']].mean(axis=1)

plt.figure(figsize=(10, 6))
sns.boxplot(x='TP_DEPENDENCIA_ADM_ESCOLA', y='MEDIA_MEDIA', data=df)
plt.title('Distribuição da Média das Notas por Tipo de Escola')
plt.xlabel('Tipo de Escola')
plt.ylabel('Média (MT, LP, CH)')
plt.savefig(f"{caminho_imagens}/boxplot_media_por_tipo_escola.png")
plt.close()

plt.figure(figsize=(10, 6))
sns.histplot(df['MEDIA_MEDIA'], kde=True, bins=30, color='steelblue')
plt.title('Distribuição das Médias (MT, LP, CH) das Escolas')
plt.xlabel('Média')
plt.ylabel('Frequência')
plt.savefig(f"{caminho_imagens}/histograma_media_geral.png")
plt.close()

plt.figure(figsize=(10, 6))
matriz = df[['NU_MEDIA_MT', 'NU_MEDIA_LP', 'NU_MEDIA_CH']].corr()
sns.heatmap(matriz, annot=True, cmap='Blues', fmt=".2f")
plt.title('Correlação entre Áreas do ENEM')
plt.savefig(f"{caminho_imagens}/heatmap_correlacao_areas.png")
plt.close()

df_top = df.sort_values(by='MEDIA_MEDIA', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x='MEDIA_MEDIA', y=df_top.index.astype(str), data=df_top, palette='viridis')
plt.title('Top 10 Escolas com Maior Média (MT, LP, CH)')
plt.xlabel('Média')
plt.ylabel('Escola (ID ou índice)')
plt.savefig(f"{caminho_imagens}/top10_escolas_media_geral.png")
plt.close()

print("Imagens do ENEM geradas com sucesso em 'imagens/'.")
