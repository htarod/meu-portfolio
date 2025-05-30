import requests

def buscar_dados_cidade(cidade):
    # Usando a API pública OpenWeatherMap (exemplo genérico com chave fictícia)
    chave_api = "sua_chave_api"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric&lang=pt_br"
    
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        temp = dados["main"]["temp"]
        descricao = dados["weather"][0]["description"]
        return f"A temperatura em {cidade} é de {temp}°C com {descricao}."
    else:
        return "Desculpe, não consegui obter os dados da cidade."

def main():
    print("Agente de IA - Previsão do Tempo")
    cidade = input("Digite o nome de uma cidade: ")
    resposta = buscar_dados_cidade(cidade)
    print("Resposta do agente:", resposta)

if __name__ == "__main__":
    main()
