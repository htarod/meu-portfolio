# Agente de IA Classificador de Mensagens

Este projeto demonstra a criação de um agente inteligente simples que classifica mensagens com base em sua **urgência** e **sentimento**, utilizando bibliotecas de NLP (Processamento de Linguagem Natural) e integração com uma API externa simulada.

---

## Propósito do Projeto

O objetivo é mostrar, de forma prática, como um agente de IA pode:

* Ler mensagens de texto como as recebidas por e-mails, SACs ou chatbots.
* Identificar mensagens urgentes com base em palavras-chave.
* Analisar o sentimento da mensagem (positivo, negativo ou neutro) com o `TextBlob`.
* Enviar os dados para uma API externa, como parte de um processo automatizado (ex: abrir chamado, redirecionar para setor, etc).

---

## Tecnologias Utilizadas

* **Python 3.10+**
* **TextBlob** – para análise de sentimentos
* **NLTK** – fornece corpora para o TextBlob
* **Requests** – para chamadas de API HTTP

---

## Como Executar Localmente

1. Clone ou copie os arquivos para sua máquina.

2. No terminal, acesse a pasta do projeto:

   ```bash
   cd projeto-agente-ia
   ```

3. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1    
   ```

4. Instale as dependências:

   ```bash
   pip install textblob requests
   python -m textblob.download_corpora
   ```

5. Execute o script:

   ```bash
   python agente_ia_classificador.py
   ```

---

## Exemplo de Saída no Terminal

```
 Análise de Mensagens Recebidas
====================================

 Mensagem 1: Minha conta foi invadida e preciso de ajuda urgente!
   ➤ Urgência: alta
   ➤ Categoria: neutra
    API chamada com status: 200

 Mensagem 2: Gostei muito do atendimento, parabéns.
   ➤ Urgência: baixa
   ➤ Categoria: elogio
    API chamada com status: 200
```

Uma captura de tela está disponível na pasta `imagens/`.

---

## Lógica de Classificação

### Urgência

Baseada em palavras-chave como: "urgente", "invadida", "ajuda", "absurdo", etc.

### Sentimento (com TextBlob)

* **Elogio**: Polarity ≥ 0.3
* **Reclamação**: Polarity ≤ -0.3
* **Neutra**: entre -0.3 e 0.3

---

## Aplicações Reais

Este projeto simula funcionalidades aplicáveis a:

* **Centros de atendimento** automatizados
* **Sistemas de Help Desk e CRM**
* **Chatbots com priorização de respostas**
* **Triagem automática de e-mails ou comentários**

Pode facilmente ser expandido para produção com:

* Base de treinamento maior
* Modelos de aprendizado de máquina customizados
* Integração com sistemas de chamados reais ou plataformas de atendimento

---

## Possíveis Expansões Futuras

* Integração com banco de dados real para armazenamento de mensagens
* Interface web com Flask ou Streamlit
* Treinamento com dataset rotulado real para sentimento e urgência

---

