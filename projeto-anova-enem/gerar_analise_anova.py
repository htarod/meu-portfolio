import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway

print("Diretório atual:", os.getcwd())

os.makedirs("imagens", exist_ok=True)

df = pd.read_csv("dados/MICRODADOS_ENEM_ESCOLA.csv", sep=";", encoding="latin1")

df_sp = df[df["SG_UF_ESCOLA"] == "SP"]

df_sp = df_sp[["TP_DEPENDENCIA_ADM_ESCOLA", "NU_MEDIA_TOT"]].dropna()

dependencias = {
    1: "Federal",
    2: "Estadual",
    3: "Municipal",
    4: "Privada"
}
df_sp["DEPENDENCIA"] = df_sp["TP_DEPENDENCIA_ADM_ESCOLA"].map(dependencias)
df_sp["MEDIA_GERAL"] = df_sp["NU_MEDIA_TOT"]

grupos = [grupo["MEDIA_GERAL"].values for nome, grupo in df_sp.groupby("DEPENDENCIA")]
f_valor, p_valor = f_oneway(*grupos)

print("Resultado do teste ANOVA:")
print(f"F = {f_valor:.2f}")
print(f"p-valor = {p_valor:.4f}")

plt.figure(figsize=(10, 6))
sns.boxplot(x="DEPENDENCIA", y="MEDIA_GERAL", data=df_sp, palette="Set2")
plt.title("Distribuição das Médias do ENEM por Dependência Administrativa (SP)")
plt.xlabel("Dependência Administrativa")
plt.ylabel("Média Geral no ENEM")
plt.tight_layout()
plt.savefig("imagens/boxplot-dependencia.png")
plt.close()

plt.figure(figsize=(10, 6))
media_por_dep = df_sp.groupby("DEPENDENCIA")["MEDIA_GERAL"].mean().sort_values()
media_por_dep.plot(kind="bar", color="skyblue")
plt.title("Média Geral do ENEM por Tipo de Escola (SP)")
plt.xlabel("Dependência Administrativa")
plt.ylabel("Média Geral")
plt.tight_layout()
plt.savefig("imagens/grafico-media-por-dependencia.png")
plt.close()
