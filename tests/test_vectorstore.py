import numpy as np
from app.vectorstore.faiss_store import FAISSVectorStore

def test_vector_search():
    store = FAISSVectorStore(3)

    embeddings = np.array([
        [1, 0, 0],
        [0, 1, 0]
    ]).astype("float32")

    store.add(embeddings, ["doc1", "doc2"])

    query = np.array([[1, 0, 0]]).astype("float32")

    results = store.search(query)

    assert results[0]["text"] == "doc1"