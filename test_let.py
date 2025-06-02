#!/usr/bin/env python

import sys
import os

# Adiciona o diretório atual ao path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Importa o módulo let
try:
    import let.cli
    print("Módulo let importado com sucesso!")
    let.cli.main()
except Exception as e:
    print(f"Erro ao importar o módulo let: {e}")