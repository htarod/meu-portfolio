from textblob import TextBlob
import requests

PALAVRAS_URGENCIA = ["urgente", "invadida", "ajuda", "absurdo", "atraso", "emergência"]

def classificar_mensagem(texto):
    blob = TextBlob(texto)
    polaridade = blob.sentiment.polarity

    if any(p in texto.lower() for p in PALAVRAS_URGENCIA):
        urgencia = "alta"
    else:
        urgencia = "baixa"

    if polaridade >= 0.3:
        categoria = "elogio"
    elif polaridade <= -0.3:
        categoria = "reclamação"
    else:
        categoria = "neutra"

    return urgencia, categoria

def acionar_api(mensagem, urgencia, categoria):
    url = "https://httpbin.org/post"  
    payload = {
        "mensagem": mensagem,
        "urgencia": urgencia,
        "categoria": categoria
    }
    response = requests.post(url, json=payload)
    return response

def main():
    mensagens = [
        "Minha conta foi invadida e preciso de ajuda urgente!",
        "Gostei muito do atendimento, parabéns.",
        "Estou esperando há dias por uma resposta. Isso é um absurdo!",
        "Olá, apenas confirmando a alteração no cadastro. Obrigado!"
    ]

    print("\n Análise de Mensagens Recebidas")
    print("====================================")

    for i, msg in enumerate(mensagens, 1):
        print(f"\n Mensagem {i}: {msg}")
        urgencia, categoria = classificar_mensagem(msg)
        print(f"   ➤ Urgência: {urgencia}")
        print(f"   ➤ Categoria: {categoria}")

        try:
            resposta = acionar_api(msg, urgencia, categoria)
            print(f"    API chamada com status: {resposta.status_code}")
        except Exception as e:
            print(f"    Erro ao chamar API: {e}")

if __name__ == "__main__":
    main()
