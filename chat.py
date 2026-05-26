import os
from dotenv import load_dotenv
import anthropic
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

LARANJA = "#d97757"
console = Console()

bichinho = """\
 ▄▄▄▄▄▄▄
█  ◉ ◉  █
█   ω   █
 ▀▄▄▄▄▄▀
  █   █
  ▀   ▀  """


def montar_painel_boas_vindas():
    texto = Text()
    texto.append("✻ ", style=LARANJA)
    texto.append("Bem-vindo ao Terminal_Code!", style="bold white")
    texto.append("\n\n")
    texto.append("  digite ", style="white")
    texto.append("sair", style=f"bold {LARANJA}")
    texto.append(" para encerrar a conversa\n", style="white")
    texto.append(f"\n  pasta: {os.getcwd()}", style="dim white")

    return Panel(
        texto,
        border_style=LARANJA,
        box=box.ROUNDED,
        padding=(0, 1),
    )


def mostrar_bichinho():
    console.print(f"[{LARANJA}]{bichinho}[/]", justify="center")
    console.print(f"[{LARANJA}]BICHINHO FOFO DO TERMINAL CODE[/]", justify="center")
    console.print()


def mostrar_boas_vindas():
    console.clear()
    console.print(montar_painel_boas_vindas())
    console.print()
    mostrar_bichinho()


def perguntar_ao_claude(cliente, pergunta):
    try:
        with console.status(f"[{LARANJA}]Pensando...[/]", spinner="dots"):
            resposta = cliente.messages.create(
                model="claude-opus-4-7",
                max_tokens=16000,
                system="Responda sempre em português do Brasil, sem markdown. Seja breve e direto ao ponto, não use emojis, e após responder, pergunte algo relacionado para manter a conversa fluindo.",
                messages=[{"role": "user", "content": pergunta}],
            )
        return next(b.text for b in resposta.content if b.type == "text")
    except anthropic.AuthenticationError:
        return "Chave da API inválida. Verifique seu .env."
    except anthropic.RateLimitError:
        return "Limite de requisições atingido. Aguarde alguns instantes."
    except anthropic.APIStatusError as e:
        if e.status_code >= 500:
            return "Servidor do Claude com problema. Tente novamente."
        return f"Erro na requisição: {e.message}"
    except Exception as e:
        return f"Ocorreu um erro inesperado: {e}"


def main():
    load_dotenv()
    cliente = anthropic.Anthropic()
    mostrar_boas_vindas()

    while True:
        pergunta = console.input(f"[{LARANJA}]> [/]")

        if pergunta.lower() == "sair":
            break

        resposta = perguntar_ao_claude(cliente, pergunta)
        console.print(f"\n[bold white]{resposta}[/]\n")


if __name__ == "__main__":
    main()
