import numpy as np
from typing import Optional, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from faq import GerenciadorFAQ
from config import logger

class MotorIA:
    """Motor de busca semântica leve utilizando TF-IDF e Similaridade de Cosseno."""
    
    def __init__(self, gerenciador_faq: GerenciadorFAQ):
        self.faq = gerenciador_faq
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = None
        self.recarregar()

    def recarregar(self) -> None:
        """Recalcula a matriz TF-IDF baseada nas perguntas atuais do FAQ."""
        perguntas = self.faq.perguntas()
        if not perguntas:
            logger.warning("IA: Nenhuma pergunta disponível para treinar o motor.")
            self.tfidf_matrix = None
            return

        try:
            self.tfidf_matrix = self.vectorizer.fit_transform(perguntas)
            logger.info("IA: Motor recarregado e treinado com sucesso.")
        except Exception as e:
            logger.error(f"IA: Erro ao treinar motor: {e}")
            self.tfidf_matrix = None

    def buscar(self, consulta: str, threshold: float = 0.2) -> Optional[str]:
        """
        Busca a resposta mais relevante para a consulta do usuário.
        
        Args:
            consulta: A pergunta feita pelo usuário.
            threshold: Valor mínimo de similaridade para considerar a resposta válida.
            
        Returns:
            A resposta correspondente ou None se não houver correspondência satisfatória.
        """
        if self.tfidf_matrix is None or not consulta:
            return None

        try:
            # Transforma a consulta do usuário no mesmo espaço vetorial
            query_vec = self.vectorizer.transform([consulta])
            
            # Calcula a similaridade de cosseno entre a consulta e todas as perguntas
            similaridades = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
            
            # Encontra o índice da maior similaridade
            indice_max = np.argmax(similaridades)
            valor_max = similaridades[indice_max]

            logger.info(f"Busca: '{consulta}' | Melhor score: {valor_max:.4f}")

            if valor_max >= threshold:
                item = self.faq.obter_item(int(indice_max))
                return item.get("resposta") if item else None
            
            return None
        except Exception as e:
            logger.error(f"IA: Erro durante a busca: {e}")
            return None
