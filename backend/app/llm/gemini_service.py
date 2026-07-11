"""
Gemini implementation of the BaseLLM interface.
"""

from google import genai

from app.core.config import settings
from app.core.logging import logger

from app.llm.base_llm import BaseLLM


class GeminiService(BaseLLM):

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        logger.info("Gemini initialized.")

    def generate(self, prompt: str) -> str:

        try:

            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            logger.info("Gemini response generated.")

            return response.text

        except Exception as e:

            logger.exception("Gemini failed.")

            raise e