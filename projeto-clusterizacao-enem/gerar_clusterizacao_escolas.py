import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

print("Diretório atual:", os.getcwd())
caminho_arquivo = os.path.join("dados", "MICRODADOS_ENEM_ESCOLA.csv")

df = pd.read_csv(caminho_arquivo, sep=";", encoding="latin1", low_memory=False)

df_sp = df[df["SG_UF_ESCOLA"] == "SP"]

colunas_cluster = [
    "NU_MEDIA_CN",   # Ciências da Natureza
    "NU_MEDIA_CH",   # Ciências Humanas
    "NU_MEDIA_LP",   # Linguagens e Códigos
    "NU_MEDIA_MT",   # Matemática
    "NU_MEDIA_RED",  # Redação
    "NU_MATRICULAS"  # Número de matrículas
]

df_cluster = df_sp[colunas_cluster].dropna()

scaler = StandardScaler()
dados_normalizados = scaler.fit_transform(df_cluster)

kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(dados_normalizados)

df_cluster["Cluster"] = clusters

os.makedirs("imagens", exist_ok=True)

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_cluster, x="NU_MEDIA_MT", y="NU_MEDIA_RED", hue="Cluster", palette="Set1")
plt.title("Clusters de Escolas (Baseado em Matemática e Redação)")
plt.xlabel("Média de Matemática")
plt.ylabel("Média de Redação")
plt.legend(title="Cluster")
plt.tight_layout()
plt.savefig("imagens/cluster-mt-redacao.png")
plt.close()

for coluna in colunas_cluster:
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="Cluster", y=coluna, data=df_cluster, palette="Set2")
    plt.title(f"Distribuição de {coluna} por Cluster")
    plt.tight_layout()
    nome_arquivo = f"imagens/boxplot_{coluna.lower()}.png"
    plt.savefig(nome_arquivo)
    plt.close()

print("Clusterização concluída. Imagens salvas na pasta 'imagens'.")
