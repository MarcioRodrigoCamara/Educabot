from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from faq import carregar_faq
from config import SIMILARIDADE_MINIMA

print("🧠 Carregando modelo de IA...")

from config import MODELO_IA, MODELOS_DIR

modelo = SentenceTransformer(
    MODELO_IA,
    cache_folder=str(MODELOS_DIR)
)

faq = carregar_faq()

perguntas = [
    item["pergunta"]
    for item in faq
]

respostas = [
    item["resposta"]
    for item in faq
]

embeddings = modelo.encode(
    perguntas,
    convert_to_tensor=False
)


def buscar_resposta(pergunta_usuario):

    embedding_usuario = modelo.encode(
        [pergunta_usuario],
        convert_to_tensor=False
    )

    similaridades = cosine_similarity(
        embedding_usuario,
        embeddings
    )[0]

    indice = similaridades.argmax()

    score = float(similaridades[indice])

    if score < SIMILARIDADE_MINIMA:

        return {
            "encontrou": False,
            "score": score,
            "resposta": None
        }

    return {

        "encontrou": True,

        "score": score,

        "resposta": respostas[indice]

    }