from textblob import TextBlob
import json


PALAVRAS_URGENCIA = ["urgente", "invadida", "ajuda", "absurdo", "atraso", "emergência"]

def classificar_mensagem(texto):
    blob = TextBlob(texto)
    polaridade = blob.sentiment.polarity

    urgencia = "alta" if any(p in texto.lower() for p in PALAVRAS_URGENCIA) else "baixa"

    if polaridade >= 0.3:
        categoria = "elogio"
    elif polaridade <= -0.3:
        categoria = "reclamação"
    else:
        categoria = "neutra"

    return urgencia, categoria

def carregar_respostas(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    mensagens = [
        "Minha conta foi invadida e preciso de ajuda urgente!",
        "Gostei muito do atendimento, parabéns.",
        "Estou esperando há dias por uma resposta. Isso é um absurdo!",
        "Olá, apenas confirmando a alteração no cadastro. Obrigado!"
    ]

    respostas = carregar_respostas("resposta_modelo.json")

    print("\n Resposta Automática Baseada na Classificação")
    print("==============================================")

    for i, msg in enumerate(mensagens, 1):
        urgencia, categoria = classificar_mensagem(msg)
        resposta = respostas.get(urgencia, {}).get(categoria, "Mensagem recebida. Em breve responderemos.")
        
        print(f"\nMensagem {i}: {msg}")
        print(f"  ➤ Urgência: {urgencia}")
        print(f"  ➤ Categoria: {categoria}")
        print(f"   Resposta sugerida: {resposta}")

if __name__ == "__main__":
    main()
