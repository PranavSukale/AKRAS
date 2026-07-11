"""
SentenceTransformer embedding provider.
"""

from sentence_transformers import SentenceTransformer

from app.embeddings.base_embedding import BaseEmbedding

from app.core.config import settings
from app.core.logging import logger


class SentenceTransformerProvider(BaseEmbedding):

    def __init__(self):

        logger.info("Loading embedding model...")

        self.model = SentenceTransformer(
            settings.EMBEDDING_MODEL
        )

        logger.info("Embedding model loaded.")

    def embed(self, texts: list[str]):

        return self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True
        )