# Terminal_Code — Chat Inteligente (Python + $\color{#d97757}{\textsf{Claude}}$)

Assistente de chat em linha de comando que usa a API do $\color{#d97757}{\textsf{Claude}}$ (Anthropic) para conversar em português do Brasil, com interface colorida no terminal.

> Projeto inspirado no [$\color{#d97757}{\textsf{Claude}}$ Code](https://claude.com/claude-code), o assistente oficial da Anthropic. Sou fã número 1!

## Funcionalidades

- Conversa interativa direto no terminal
- Respostas em português do Brasil, breves e diretas
- Interface estilizada com a biblioteca `rich` (painel de boas-vindas, mascote ASCII, cor laranja)
- Spinner "Pensando..." enquanto aguarda a resposta do modelo
- IA treinada para fazer perguntas de volta e manter a conversa fluindo
- Tratamento de erros amigável (sem traceback gigante quando algo dá errado)
- Encerramento simples digitando `sair`

## Requisitos

- Python 3.10+
- Chave da API do $\color{#d97757}{\textsf{Claude}}$ (criada em [console.anthropic.com](https://console.anthropic.com/))

> ⚠️ **A API do $\color{#d97757}{\textsf{Claude}}$ é paga.** Cada pessoa precisa criar a própria chave e adicionar créditos na conta. O custo é por token usado (centavos por conversa típica), mas é responsabilidade de quem roda. Eu **não** compartilho minha chave — se quiser usar o projeto, traga a sua.

## Instalação

1. Clone o repositório e entre na pasta do projeto:

   ```bash
   git clone https://github.com/matheuseduardo04-dotcom/Terminal_Code.git
   cd Terminal_Code
   ```

2. (Opcional) Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install python-dotenv anthropic rich
   ```

## Configuração

1. Crie sua chave em [console.anthropic.com](https://console.anthropic.com/) → **API Keys** → **Create Key**.
2. Adicione créditos em **Billing** (a Anthropic não tem tier grátis).
3. Crie um arquivo `.env` na raiz do projeto com sua chave:

   ```env
   ANTHROPIC_API_KEY=sk-ant-...
   ```

   > ⚠️ **Nunca commite o `.env`.** Ele já está no `.gitignore` deste projeto, mas confira.

## Como usar

Execute o script:

```bash
python chat.py
```

Digite sua pergunta no `>` e pressione Enter. Para sair, digite:

```
sair
```

## Estrutura

```
Terminal_Code/
├── .env          # Variáveis de ambiente (não versionar)
├── .gitignore
├── chat.py       # Código principal do chat
└── README.md     # Este arquivo
```

## Modelo utilizado

`claude-opus-4-7` — o modelo mais capaz da Anthropic. Configurado via `system prompt` para responder em português do Brasil, sem markdown, sem emojis, e perguntando algo de volta para manter a conversa fluindo.
