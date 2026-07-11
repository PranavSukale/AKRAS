from app.llm.factory import LLMFactory


llm = LLMFactory.create()

answer = llm.generate(
    "Explain embeddings in one paragraph."
)

print(answer)