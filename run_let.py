#!/usr/bin/env python

import sys
import os

# Adiciona o diretório atual ao path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Importa o CLI e executa o comando
from cli import cli

if __name__ == "__main__":
    cli()  # Executa o CLI diretamente, sem argumentos