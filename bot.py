"""
Telegram
EducaBot 3.0
"""

import logging

from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import (
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)

from ia import buscar_resposta, recarregar

logger = logging.getLogger("EducaBot")


# ===========================================
# /start
# ===========================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(

        "👋 Olá!\n\n"

        "Sou o EducaBot 🤖\n\n"

        "Assistente Virtual do Educacenso.\n\n"

        "Digite sua pergunta."

    )


# ===========================================
# /help
# ===========================================

async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(

        "Comandos disponíveis:\n\n"

        "/start\n"

        "/help\n"

        "/reload"

    )


# ===========================================
# /reload
# ===========================================

async def reload(update: Update, context: ContextTypes.DEFAULT_TYPE):

    recarregar()

    await update.message.reply_text(

        "✅ FAQ atualizado."

    )


# ===========================================
# Mensagens
# ===========================================

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):

    pergunta = update.message.text.strip()

    logger.info(
        "Pergunta: %s",
        pergunta
    )

    await context.bot.send_chat_action(

        chat_id=update.effective_chat.id,

        action=ChatAction.TYPING

    )

    resultado = buscar_resposta(pergunta)

    logger.info(
        "Similaridade %.3f",
        resultado["score"]
    )

    await update.message.reply_text(

        resultado["resposta"]

    )


# ===========================================
# Erros
# ===========================================

async def erro(update, context):

    logger.exception(context.error)


# ===========================================
# Registrar
# ===========================================

def registrar_handlers(app):

    app.add_handler(

        CommandHandler(
            "start",
            start
        )

    )

    app.add_handler(

        CommandHandler(
            "help",
            ajuda
        )

    )

    app.add_handler(

        CommandHandler(
            "reload",
            reload
        )

    )

    app.add_handler(

        MessageHandler(

            filters.TEXT & ~filters.COMMAND,

            responder

        )

    )

    app.add_error_handler(

        erro

    )