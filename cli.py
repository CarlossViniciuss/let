import click
import sys
import os

# Adiciona o diretório pai ao path para permitir imports relativos
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Usando apenas imports relativos
from config import get_api_key
from prompts import ask_questions
from main import generate_tests

@click.command()
def cli():
    """Let - Gerador de Testes Automatizados"""
    click.clear()
    click.echo("🚀 Bem-vindo ao Let - Gerador de Testes Automatizados")
    api_key = get_api_key()
    answers = ask_questions()
    generate_tests(api_key, answers)

def main():
    cli()

if __name__ == "__main__":
    main()
