import logging

from telegram.ext import ApplicationBuilder

from config import (
    TOKEN,
    PORT,
    WEBHOOK_URL,
)

from bot import registrar_handlers

logging.basicConfig(

    format="%(asctime)s - %(levelname)s - %(message)s",

    level=logging.INFO

)

logger = logging.getLogger(__name__)


def criar_app():

    app = (

        ApplicationBuilder()

        .token(TOKEN)

        .build()

    )

    registrar_handlers(app)

    return app


def main():

    logger.info("🤖 Iniciando EducaBot...")

    app = criar_app()

    if WEBHOOK_URL:

        logger.info("🌎 Executando em Webhook")

        app.run_webhook(

            listen="0.0.0.0",

            port=PORT,

            webhook_url=WEBHOOK_URL,

            secret_token="educabot"

        )

    else:

        logger.info("💻 Executando localmente")

        app.run_polling()


if __name__ == "__main__":

    main()