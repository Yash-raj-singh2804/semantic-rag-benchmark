from abc import ABC, abstractmethod
from typing import List
import numpy as np

class BaseEmbeddingModel(ABC):
    @abstractmethod
    def embed(self, texts: List[str]) -> np.ndarray:
        pass