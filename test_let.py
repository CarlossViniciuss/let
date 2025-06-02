import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

try:
    import let.cli
    print("Módulo let importado com sucesso!")
    let.cli.main()
except Exception as e:
    print(f"Erro ao importar o módulo let: {e}")