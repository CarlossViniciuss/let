import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from cli import cli

if __name__ == "__main__":
    cli() 