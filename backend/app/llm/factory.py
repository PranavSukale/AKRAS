"""
Factory for creating LLM providers.
"""

from app.llm.gemini_service import GeminiService


class LLMFactory:

    @staticmethod
    def create():

        return GeminiService()