# Chat Inteligente (Python + Gemini)

Assistente de chat em linha de comando que usa a API do Google Gemini para responder perguntas em português do Brasil, com interface colorida no terminal.

## Funcionalidades

- Conversa interativa direto no terminal
- Respostas em português do Brasil, breves e diretas
- Saída estilizada com cor laranja e mascote em ASCII
- Encerramento simples digitando `sair`

## Requisitos

- Python 3.10+
- Conta com chave de API do Google Gemini

## Instalação

1. Clone o repositório e entre na pasta do projeto:

   ```bash
   cd chat.inteligente_py
   ```

2. (Opcional) Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install python-dotenv google-genai
   ```

## Configuração

Crie um arquivo `.env` na raiz do projeto com sua chave da API:

```env
GEMINI_API_KEY=sua_chave_aqui
```

## Como usar

Execute o script:

```bash
python chat.py
```

Digite sua pergunta no terminal e pressione Enter. Para sair, digite:

```
sair
```

## Estrutura

```
chat.inteligente_py/
├── .env          # Variáveis de ambiente (não versionar)
├── chat.py       # Código principal do chat
└── README.md     # Este arquivo
```

## Modelo utilizado

`gemini-2.5-flash` — configurado para responder em português do Brasil, sem markdown e sem emojis.
