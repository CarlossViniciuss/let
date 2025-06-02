import os
import json
from pathlib import Path

CONFIG_FILE = Path.home() / ".let_config.json"

def get_api_key():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)
            return data.get("api_key")

    api_key = input("🔑 Insira sua API Key da Groq: ").strip()
    with open(CONFIG_FILE, "w") as f:
        json.dump({"api_key": api_key}, f)
    return api_key
