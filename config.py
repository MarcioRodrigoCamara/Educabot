import os

TOKEN = os.getenv("TOKEN")

PORT = int(os.getenv("PORT", 10000))

WEBHOOK_URL = os.getenv("RENDER_EXTERNAL_URL")

SIMILARIDADE_MINIMA = 0.55

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

FAQ_FILE = BASE_DIR / "dados" / "faq.json"

MODELO_IA = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

MODELOS_DIR = BASE_DIR / "modelos"

LOGS_DIR = BASE_DIR / "logs"