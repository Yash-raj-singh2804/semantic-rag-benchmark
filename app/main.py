from app.embeddings.sentence_transformer import (
    SentenceTransformerEmbedding
)
from app.vectorstore.faiss_store import FAISSVectorStore
from app.ingestion.loader import load_documents
from app.ingestion.chunker import chunk_text
from app.retrieval.retriever import Retriever
from app.retrieval.benchmark import BenchmarkRunner
import json

def main():
    text = load_documents("data/technical_docs.txt")

    chunks = chunk_text(text)

    embedding_model = SentenceTransformerEmbedding()

    embeddings = embedding_model.embed(chunks)

    dimension = embeddings.shape[1]

    vector_store = FAISSVectorStore(dimension)

    vector_store.add(embeddings, chunks)

    retriever = Retriever(
        embedding_model=embedding_model,
        vector_store=vector_store
    )

    benchmark_runner = BenchmarkRunner(retriever)

    queries = [
        "How does the system handle peak load?",
        "What happens during database failure?",
        "How is latency reduced?"
    ]

    results = benchmark_runner.run(queries)

    print(json.dumps(
        [result.dict() for result in results],
        indent=2
    ))

if __name__ == "__main__":
    main()