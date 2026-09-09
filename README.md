# 🛒 ExemploMart - Chatbot de Supermercado

Chatbot de atendimento para um supermercado fictício, desenvolvido em Python com Flask e integração com a API do Google Gemini.

## Funcionalidades

- Chat simples via navegador para tirar dúvidas sobre produtos, preços, promoções e horário de funcionamento
- Backend em Flask que se comunica com a API do Gemini
- Testes unitários cobrindo a lógica do bot e a rota de chat

## Tecnologias utilizadas

- Python 3
- Flask
- Google Gemini API (google-genai)
- python-dotenv
- HTML, CSS e JavaScript puro (frontend)
- pytest (testes unitários)

## Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/yagoferb48-jpg/chatbot-supermercado.git
cd chatbot-supermercado
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\Activate.ps1
```

Linux/Mac:
```bash
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a chave da API

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
> Você pode gerar uma chave gratuita em [Google AI Studio](https://aistudio.google.com/apikey).
> **Importante:** o arquivo `.env` não é versionado (está no `.gitignore`) para não expor a chave publicamente.

### 5. Rode a aplicação

```bash
python app.py
```

Acesse **http://127.0.0.1:5000** no navegador.

## Como rodar os testes

```bash
pytest tests/ -v
```

## Estrutura do projeto
hatbot-supermercado/
├── app.py # Backend Flask + integração com Gemini
├── conftest.py # Configuração do pytest
├── requirements.txt
├── .env # Chave da API (não versionado)
├── .gitignore
├── templates/
│ └── index.html # Interface do chat
├── static/
│ ├── style.css
│ └── script.js
└── tests/
└── test_chatbot.py # Testes unitários

## Autor

Yago Ferb ([@yagoferb48-jpg](https://github.com/yagoferb48-jpg))