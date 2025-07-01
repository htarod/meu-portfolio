
import pandas as pd

caminho_csv_original = "dados/MICRODADOS_ENEM_ESCOLA.csv"

df = pd.read_csv(caminho_csv_original, sep=';', encoding='latin1')

colunas_selecionadas = {
    'SG_UF_ESCOLA': 'uf',
    'NO_MUNICIPIO_ESCOLA': 'municipio',
    'TP_DEPENDENCIA_ADM_ESCOLA': 'cod_tipo_escola',
    'NU_MEDIA_MT': 'media_matematica',
    'NU_MEDIA_CH': 'media_humanas',
    'NU_MEDIA_LP': 'media_linguagens'
}

df = df[list(colunas_selecionadas.keys())].rename(columns=colunas_selecionadas)

df = df.dropna()

df['tipo_escola'] = df['cod_tipo_escola'].map({
    1: 'Federal',
    2: 'Estadual',
    3: 'Municipal',
    4: 'Privada'
})

df['media_geral'] = df[['media_matematica', 'media_humanas', 'media_linguagens']].mean(axis=1).round(2)

colunas_finais = ['uf', 'municipio', 'tipo_escola', 'media_matematica', 'media_humanas', 'media_linguagens', 'media_geral']
df = df[colunas_finais]

caminho_saida = "dados/enem_tratado.csv"
df.to_csv(caminho_saida, index=False)

print("Arquivo 'enem_tratado.csv' gerado com sucesso.")
