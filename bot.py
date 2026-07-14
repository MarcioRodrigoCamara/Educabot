import logging

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from ia import buscar_resposta

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


# ===============================
# /start
# ===============================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(

        "👋 Olá!\n\n"

        "Sou o EducaBot 🤖\n\n"

        "Posso responder dúvidas sobre o Educacenso.\n\n"

        "Digite sua pergunta."

    )


# ===============================
# Responder mensagens
# ===============================

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):

    pergunta = update.message.text.strip()

    resultado = buscar_resposta(pergunta)

    logger.info(
        "Pergunta: %s | Score: %.3f",
        pergunta,
        resultado["score"]
    )

    if resultado["encontrou"]:

        await update.message.reply_text(
            resultado["resposta"]
        )

        return

    await update.message.reply_text(

        "❌ Não encontrei essa informação no FAQ.\n\n"

        "Reformule a pergunta ou entre em contato com o suporte."

    )


# ===============================
# Registrar Handlers
# ===============================

def registrar_handlers(app: Application):

    app.add_handler(

        CommandHandler(
            "start",
            start
        )

    )

    app.add_handler(

        MessageHandler(

            filters.TEXT & ~filters.COMMAND,

            responder

        )

    )