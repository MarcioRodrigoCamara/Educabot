import json
from pathlib import Path

# Caminho da pasta do projeto
BASE_DIR = Path(__file__).resolve().parent

# Caminho do FAQ
FAQ_FILE = BASE_DIR / "dados" / "faq.json"


def carregar_faq():
    """
    Carrega o FAQ em memória.
    """

    if not FAQ_FILE.exists():
        raise FileNotFoundError(
            f"Arquivo não encontrado: {FAQ_FILE}"
        )

    with open(FAQ_FILE, "r", encoding="utf-8") as arquivo:
        faq = json.load(arquivo)

    return faq


def perguntas():
    faq = carregar_faq()
    return [item["pergunta"] for item in faq]


def respostas():
    faq = carregar_faq()
    return [item["resposta"] for item in faq]