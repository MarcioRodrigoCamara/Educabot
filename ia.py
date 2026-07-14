"""
Motor de IA
EducaBot 3.0
"""

import logging

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from config import (
    MODELO_IA,
    MODELOS_DIR,
    SIMILARIDADE_MINIMA,
)

from faq import faq

logger = logging.getLogger("EducaBot")

logger.info("Carregando modelo de IA...")

modelo = SentenceTransformer(
    MODELO_IA,
    cache_folder=str(MODELOS_DIR)
)

logger.info("Gerando embeddings...")

perguntas = faq.perguntas()

respostas = faq.respostas()

embeddings = modelo.encode(
    perguntas,
    normalize_embeddings=True
)

logger.info(
    "%s embeddings gerados.",
    len(embeddings)
)


def buscar_resposta(pergunta: str):

    if not pergunta.strip():

        return {

            "encontrou": False,

            "score": 0.0,

            "resposta": "Digite uma pergunta."

        }

    embedding = modelo.encode(
        [pergunta],
        normalize_embeddings=True
    )

    similaridades = cosine_similarity(
        embedding,
        embeddings
    )[0]

    indice = similaridades.argmax()

    score = float(
        similaridades[indice]
    )

    logger.info(
        "Similaridade %.3f",
        score
    )

    if score < SIMILARIDADE_MINIMA:

        return {

            "encontrou": False,

            "score": score,

            "resposta": (
                "Não encontrei essa informação "
                "no FAQ."
            )

        }

    return {

        "encontrou": True,

        "score": score,

        "resposta": respostas[indice]

    }


def recarregar():

    global perguntas
    global respostas
    global embeddings

    faq.carregar()

    perguntas = faq.perguntas()

    respostas = faq.respostas()

    embeddings = modelo.encode(
        perguntas,
        normalize_embeddings=True
    )

    logger.info(
        "Embeddings atualizados."
    )