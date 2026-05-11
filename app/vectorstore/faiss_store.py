import faiss
import numpy as np
from typing import List

class FAISSVectorStore:
    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatIP(dimension)
        self.documents = []

    def add(self, embeddings: np.ndarray, documents: List[str]):
        self.index.add(embeddings.astype(np.float32))
        self.documents.extend(documents)

    def search(self, query_embedding: np.ndarray, top_k: int = 3):

        scores, indices = self.index.search(
            query_embedding.astype(np.float32),
            top_k
        )

        results = []

        for score, idx in zip(scores[0], indices[0]):
            results.append({
                "text": self.documents[idx],
                "score": float(score)
            })

        return results