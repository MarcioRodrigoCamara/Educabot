"""
Gerenciamento do FAQ
EducaBot 3.0
"""

import json
import logging

from config import FAQ_FILE

logger = logging.getLogger("EducaBot")


class FAQ:

    def __init__(self):

        self.dados = []

        self.carregar()

    def carregar(self):

        logger.info("Carregando FAQ...")

        try:

            with open(
                FAQ_FILE,
                "r",
                encoding="utf-8"
            ) as arquivo:

                self.dados = json.load(arquivo)

        except FileNotFoundError:

            logger.error(
                "FAQ não encontrado."
            )

            self.dados = []

        except Exception as erro:

            logger.exception(erro)

            self.dados = []

        logger.info(
            "%s perguntas carregadas.",
            len(self.dados)
        )

    def perguntas(self):

        return [

            item["pergunta"]

            for item in self.dados

        ]

    def respostas(self):

        return [

            item["resposta"]

            for item in self.dados

        ]

    def quantidade(self):

        return len(self.dados)


faq = FAQ()