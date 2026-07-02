"""
Application Configuration

This module loads all environment variables from the .env file
and exposes them through a single Settings object.
"""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


# Project Root (AKRAS/)
BASE_DIR = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """

    APP_NAME: str = "AKRAS"
    APP_VERSION: str = "1.0.0"

    GEMINI_API_KEY: str

    EMBEDDING_MODEL: str = "BAAI/bge-small-en-v1.5"

    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 100

    TOP_K_RESULTS: int = 5

    VECTOR_DB_PATH: str = "data/faiss_index"

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        extra="ignore",
    )


settings = Settings()