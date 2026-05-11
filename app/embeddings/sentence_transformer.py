from sentence_transformers import SentenceTransformer
from .base import BaseEmbeddingModel
from typing import List
import numpy as np

class SentenceTransformerEmbedding(BaseEmbeddingModel):
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed(self, texts: List[str]) -> np.ndarray:
        embeddings = self.model.encode(texts, normalize_embeddings=True)
        return np.array(embeddings)