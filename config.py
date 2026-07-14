"""
Configurações do EducaBot 3.0
"""

import os
from pathlib import Path

# =====================================================
# Diretórios
# =====================================================

BASE_DIR = Path(__file__).resolve().parent

DADOS_DIR = BASE_DIR / "dados"

LOGS_DIR = BASE_DIR / "logs"

MODELOS_DIR = BASE_DIR / "modelos"

FAQ_FILE = DADOS_DIR / "faq.json"

# =====================================================
# Telegram
# =====================================================

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise RuntimeError(
        "A variável TOKEN não foi configurada."
    )

# =====================================================
# Servidor
# =====================================================

PORT = int(
    os.getenv(
        "PORT",
        "10000"
    )
)

RENDER_EXTERNAL_URL = os.getenv(
    "RENDER_EXTERNAL_URL"
)

# =====================================================
# IA
# =====================================================

MODELO_IA = (
    "sentence-transformers/"
    "paraphrase-multilingual-MiniLM-L12-v2"
)

SIMILARIDADE_MINIMA = 0.60

# =====================================================
# Criação automática das pastas
# =====================================================

LOGS_DIR.mkdir(
    exist_ok=True
)

MODELOS_DIR.mkdir(
    exist_ok=True
)