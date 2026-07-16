import json
import logging
from typing import List, Dict, Optional
from config import FAQ_JSON_PATH, logger

class GerenciadorFAQ:
    """Classe responsável por carregar e gerenciar o conteúdo do FAQ."""
    
    def __init__(self):
        self._faq_data: List[Dict[str, str]] = []
        self.carregar()

    def carregar(self) -> None:
        """Carrega os dados do arquivo JSON do FAQ."""
        try:
            if not FAQ_JSON_PATH.exists():
                logger.warning(f"Arquivo FAQ não encontrado em {FAQ_JSON_PATH}. Iniciando vazio.")
                self._faq_data = []
                return

            with open(FAQ_JSON_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    self._faq_data = data
                    logger.info(f"FAQ carregado com sucesso: {len(self._faq_data)} itens.")
                else:
                    logger.error("Formato de JSON inválido no FAQ. Esperado uma lista de objetos.")
                    self._faq_data = []
        except Exception as e:
            logger.error(f"Erro ao carregar FAQ: {e}", exc_info=True)
            self._faq_data = []

    def perguntas(self) -> List[str]:
        """Retorna uma lista com todas as perguntas do FAQ."""
        return [item.get("pergunta", "") for item in self._faq_data if "pergunta" in item]

    def respostas(self) -> List[str]:
        """Retorna uma lista com todas as respostas do FAQ."""
        return [item.get("resposta", "") for item in self._faq_data if "resposta" in item]

    def obter_item(self, index: int) -> Optional[Dict[str, str]]:
        """Retorna um item específico do FAQ pelo índice."""
        try:
            return self._faq_data[index]
        except IndexError:
            return None

    def recarregar(self) -> bool:
        """Recarrega os dados do FAQ do disco."""
        logger.info("Recarregando FAQ...")
        self.carregar()
        return len(self._faq_data) > 0
