import pandas as pd
import spacy
import matplotlib.pyplot as plt
from collections import Counter
import os

nlp = spacy.load("pt_core_news_sm")

dados_path = "dados/reclamacoes_completas.csv"

df = pd.read_csv(dados_path)
coluna_texto = df.columns[0] 
textos = df[coluna_texto].dropna().astype(str).head(300)  

entidades = []

for texto in textos:
    doc = nlp(texto)
    for ent in doc.ents:
        if ent.label_ in ['ORG', 'LOC', 'MONEY']:
            entidades.append((ent.text.strip(), ent.label_))

entidades_filtradas = [
    e for e in entidades if e[0].lower() not in ['editado', 'title', 'propaganda', 'comprei']
]

entidades_texto = [e[0] for e in entidades_filtradas]
contagem = Counter(entidades_texto).most_common(10)


entidades_plot, frequencias = zip(*contagem)
plt.figure(figsize=(10, 6))
plt.barh(entidades_plot[::-1], frequencias[::-1])
plt.title('Entidades Mais Citadas (ORG, LOC, MONEY)')
plt.xlabel('Frequência')
plt.tight_layout()

os.makedirs("projeto-ner/imagens", exist_ok=True)
plt.savefig("imagens/grafico_entidades.png")
plt.close()

print("Gráfico salvo com sucesso em projeto-ner/imagens/grafico_entidades.png")
