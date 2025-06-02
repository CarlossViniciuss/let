from rich.prompt import Prompt

def ask_questions():
    framework = Prompt.ask("🧪 Qual framework você está usando?", choices=["pytest", "playwright", "robot", "behave"])
    descricao = Prompt.ask("📋 Descreva brevemente as regras, fluxos e possíveis cenários de teste")
    return {"framework": framework, "descricao": descricao}
