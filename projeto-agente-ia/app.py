import streamlit as st
from textblob import TextBlob
import json

# ====== respostas automáticas ======
def carregar_respostas(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

# ====== classificar  ======
def classificar_mensagem(texto):
    palavras_urgencia = ["urgente", "invadida", "ajuda", "absurdo", "atraso", "emergência"]
    blob = TextBlob(texto)
    polaridade = blob.sentiment.polarity

    urgencia = "alta" if any(p in texto.lower() for p in palavras_urgencia) else "baixa"

    if polaridade >= 0.3:
        categoria = "elogio"
    elif polaridade <= -0.3:
        categoria = "reclamação"
    else:
        categoria = "neutra"

    return urgencia, categoria

# ====== streamlit ======
st.set_page_config(page_title="Agente de IA - Classificação e Resposta", layout="centered")

st.title(" Agente de IA - Classificação de Mensagens com Resposta Automática")

st.write("Digite uma mensagem recebida de um cliente e veja a classificação da urgência, o sentimento e uma resposta sugerida.")

mensagem = st.text_area(" Mensagem recebida", height=150)

if st.button("Classificar e Responder"):
    if not mensagem.strip():
        st.warning("Digite uma mensagem para classificar.")
    else:
        respostas = carregar_respostas("resposta_modelo.json")
        urgencia, categoria = classificar_mensagem(mensagem)
        resposta = respostas.get(urgencia, {}).get(categoria, "Mensagem recebida. Em breve responderemos.")

        st.markdown("###  Classificação da Mensagem")
        st.write(f"**Urgência:** `{urgencia}`")
        st.write(f"**Categoria:** `{categoria}`")

        st.markdown("###  Resposta Sugerida")
        st.success(resposta)
