"""
EducaBot 3.0
Autor: Márcio Rodrigo Câmara

Arquivo principal
"""

import logging
import os

from telegram.ext import Application

from config import TOKEN
from bot import registrar_handlers

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("EducaBot")


def criar_aplicacao() -> Application:

    app = (
        Application.builder()
        .token(TOKEN)
        .build()
    )

    registrar_handlers(app)

    return app


def executar():

    logger.info("=" * 60)
    logger.info("🤖 EducaBot 3.0")
    logger.info("=" * 60)

    app = criar_aplicacao()

    # Render
    if os.getenv("RENDER"):

        logger.info("Modo Render")

        app.run_webhook(

            listen="0.0.0.0",

            port=int(os.getenv("PORT", 10000)),

            url_path=TOKEN,

            webhook_url=f"{os.getenv('RENDER_EXTERNAL_URL')}/{TOKEN}"

        )

    else:

        logger.info("Modo Local")

        app.run_polling(
            allowed_updates=Application.ALL_TYPES
        )


if __name__ == "__main__":

    executar()