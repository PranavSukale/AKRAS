from app.core.config import settings

print(settings.APP_NAME)
print(settings.APP_VERSION)
print(settings.GEMINI_API_KEY[:10])
print(settings.EMBEDDING_MODEL)
print(settings.CHUNK_SIZE)