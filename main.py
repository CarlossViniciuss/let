# Imports condicionais para funcionar tanto como módulo quanto como script direto
try:
    from let.generator import behave_generator, pytest_generator, robot_generator, playwright_generator
except ModuleNotFoundError:
    from generator import behave_generator, pytest_generator, robot_generator, playwright_generator

def generate_tests(api_key, answers):
    framework = answers["framework"]
    descricao = answers["descricao"]

    if framework == "behave":
        behave_generator.generate(api_key, descricao)
    elif framework == "pytest":
        pytest_generator.generate(api_key, descricao)
    elif framework == "robot":
        robot_generator.generate(api_key, descricao)
    elif framework == "playwright":
        playwright_generator.generate(api_key, descricao)
