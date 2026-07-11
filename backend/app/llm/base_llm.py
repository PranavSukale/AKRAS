"""
Base interface for all LLM providers.
"""

from abc import ABC, abstractmethod


class BaseLLM(ABC):
    """
    Abstract interface that every LLM provider must implement.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate a response from an LLM.

        Args:
            prompt: Input prompt.

        Returns:
            Generated text.
        """
        pass    