from app.embeddings.factory import EmbeddingFactory


embedder = EmbeddingFactory.create()

vectors = embedder.embed([
    "Artificial Intelligence",
    "Machine Learning"
])

print(vectors.shape)