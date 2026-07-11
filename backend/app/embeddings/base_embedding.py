"""
Base interface for embedding providers.
"""

from abc import ABC, abstractmethod


class BaseEmbedding(ABC):

    @abstractmethod
    def embed(self, texts: list[str]):
        """
        Generate embeddings.
        """
        pass