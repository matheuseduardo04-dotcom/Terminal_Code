from dotenv import load_dotenv
from google import genai
from google.genai import types
from rich.console import Console
from rich.prompt import Prompt

LARANJA = "#d97757"
console = Console()

bichinho = """\
 ▄▄▄▄▄▄▄
█  ◉ ◉  █
█   ω   █
 ▀▄▄▄▄▄▀
  █   █
  ▀   ▀  """


def mostrar_boas_vindas():
    console.clear()
    console.print("[bold white]Bem vindo Matheus![/]", justify="center")
    console.print()
    console.print(f"[{LARANJA}]{bichinho}[/]", justify="center")
    console.print(f"[{LARANJA}]Olá! Sou seu assistente.[/]", justify="center")
    console.print()


def perguntar_ao_gemini(cliente, pergunta):
    with console.status(f"[{LARANJA}]Pensando...[/]", spinner="dots"):
        resposta = cliente.models.generate_content(
            model="gemini-2.5-flash",
            contents=pergunta,
            config=types.GenerateContentConfig(
                system_instruction="Responda sempre em português do Brasil, e sem o  *markdown**. Seja breve e direto ao ponto, e não use emojis.",
            ),
        )
    return resposta.text


def main():
    load_dotenv()
    cliente = genai.Client()
    mostrar_boas_vindas()

    while True:
        pergunta = Prompt.ask(f"[{LARANJA}][/]")

        if pergunta.lower() == "sair":
            break

        resposta = perguntar_ao_gemini(cliente, pergunta)
        console.print(f"\n[{LARANJA}]{resposta}[/]\n")


if __name__ == "__main__":
    main()
