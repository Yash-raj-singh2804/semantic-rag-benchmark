from pydantic import BaseModel
from typing import List

class DocumentChunk(BaseModel):
    id: int
    text: str

class RetrievalResult(BaseModel):
    text: str
    score: float

class BenchmarkResult(BaseModel):
    query: str
    expanded_query: str
    strategy_a_results: List[RetrievalResult]
    strategy_b_results: List[RetrievalResult]