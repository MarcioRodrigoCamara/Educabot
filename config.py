import os
import logging
from pathlib import Path

# Base Directory
BASE_DIR = Path(__file__).resolve().parent

# Configurações do Telegram
TOKEN = os.getenv("TELEGRAM_TOKEN", "")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "")  # URL do Render (ex: https://meu-app.onrender.com)

# Configurações do Servidor
PORT = int(os.getenv("PORT", 8000))

# Configurações de Dados
DADOS_DIR = BASE_DIR / "dados"
FAQ_JSON_PATH = DADOS_DIR / "faq.json"

# Configurações de Logs
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "educabot.log"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

# Garantir que os diretórios existam
DADOS_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

# Configuração de Logging
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("EducaBot")
