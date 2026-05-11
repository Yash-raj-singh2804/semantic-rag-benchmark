# 🚀 Teleport RAG Engine
### Semantic Retrieval-Augmented Generation (RAG) & Vector Search Benchmark

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/FAISS-Vector_Search-green" />
  <img src="https://img.shields.io/badge/SentenceTransformers-Embeddings-orange" />
  <img src="https://img.shields.io/badge/Status-Completed-success" />
</p>

---

# 📌 Overview

Teleport RAG Engine is a local Retrieval-Augmented Generation (RAG) system built for semantic search experimentation and benchmarking.

The project demonstrates:

✅ Embedding generation  
✅ Vector similarity search  
✅ Query expansion  
✅ Retrieval benchmarking  
✅ Mocked Vertex AI behavior  
✅ Production-oriented architecture  

The system compares two retrieval strategies:

| Strategy | Description |
|---|---|
| **Strategy A** | Raw vector similarity search |
| **Strategy B** | AI-enhanced query expansion before retrieval |

---

# 🧠 Problem Statement

Modern search systems often fail when:
- user queries are vague
- wording differs from indexed documents
- semantic meaning is implicit

This project evaluates whether query expansion improves retrieval relevance in a semantic RAG pipeline.

---

# 🏗️ System Architecture

```text
                    ┌─────────────────┐
                    │ Technical Docs  │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │ Text Chunking   │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │ Embeddings      │
                    │ sentence-transformers
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │ FAISS Vector DB │
                    └────────┬────────┘
                             │
        ┌────────────────────┴────────────────────┐
        │                                         │
┌───────▼────────┐                       ┌────────▼────────┐
│ Strategy A     │                       │ Strategy B      │
│ Raw Search     │                       │ Query Expansion │
└───────┬────────┘                       └────────┬────────┘
        │                                         │
        └────────────────┬────────────────────────┘
                         │
                ┌────────▼────────┐
                │ Benchmark Engine │
                └─────────────────┘
```

---

# ⚡ Features

## 🔹 Embedding Generation
- Uses `sentence-transformers`
- Local embedding generation
- Cosine similarity optimized

---

## 🔹 Vector Search
- FAISS-based retrieval
- Efficient similarity search
- Top-K semantic retrieval

---

## 🔹 Query Expansion
Simulates:
- Gemini / Vertex AI query rewriting
- Semantic enrichment
- Context-aware retrieval optimization

Example:

| Original Query | Expanded Query |
|---|---|
| How does the system handle peak load? | autoscaling, traffic spikes, throughput balancing |

---

## 🔹 Benchmarking
Compares:
- relevance scores
- ranking improvements
- retrieval quality

---

# 📂 Project Structure

```text
Teleport_RAG_Engine/
│
├── app/
│   ├── embeddings/
│   ├── retrieval/
│   ├── vectorstore/
│   ├── ingestion/
│   ├── models/
│   ├── utils/
│   └── main.py
│
├── data/
│   └── technical_docs.txt
│
├── tests/
│   ├── test_retrieval.py
│   ├── test_vectorstore.py
│   └── test_query_expansion.py
│
├── retrieval_benchmark.md
├── requirements.txt
├── README.md
└── .env.example
```

---

# 🧪 Benchmark Example

## Query
```text
How does the system handle peak load?
```

---

## Strategy A — Raw Search

| Rank | Result | Score |
|---|---|---|
| 1 | Autoscaling groups handle traffic spikes | 0.62 |
| 2 | Load balancers distribute requests | 0.48 |
| 3 | Message queues buffer workloads | 0.30 |

---

## Strategy B — Query Expansion

Expanded Query:

```text
system scalability autoscaling traffic spikes throughput balancing
```

| Rank | Result | Score |
|---|---|---|
| 1 | Autoscaling groups handle traffic spikes | 0.78 |
| 2 | Load balancers distribute requests | 0.54 |
| 3 | Message queues buffer workloads | 0.40 |

---

# 📈 Observation

Query expansion significantly improves:
- semantic relevance
- similarity scores
- contextual retrieval accuracy

---

# 🔍 Why Cosine Similarity?

The system uses:

```python
faiss.IndexFlatIP
```

with normalized embeddings.

This effectively computes cosine similarity.

## Advantages

✅ Magnitude independent  
✅ Better semantic matching  
✅ Industry standard for embeddings  

---

# 🧱 Technologies Used

| Component | Technology |
|---|---|
| Language | Python 3.10 |
| Embeddings | sentence-transformers |
| Vector DB | FAISS |
| Testing | Pytest |
| Validation | Pydantic |
| Logging | Loguru |

---

# 🚀 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Yash-raj-singh2804/semantic-rag-benchmark
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv myvenv
myvenv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv myvenv
source myvenv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

```bash
python -m app.main
```

---

# ✅ Example Output

```json
[
  {
    "query": "How does the system handle peak load?",
    "expanded_query": "system scalability autoscaling traffic spikes throughput balancing",
    "strategy_a_results": [...],
    "strategy_b_results": [...]
  }
]
```

---

# 🧪 Running Tests

```bash
pytest
```

---

# 🧠 Mocked Vertex AI Components

This project mocks:

| Vertex AI Service | Local Equivalent |
|---|---|
| TextEmbeddingModel | sentence-transformers |
| GenerativeModel | QueryExpander |

This enables:
- local experimentation
- offline testing
- reproducible benchmarking

---

# ☁️ Production Migration Plan

## Current Local Stack

| Local | Production |
|---|---|
| sentence-transformers | Vertex AI Embeddings |
| FAISS | Vertex AI Matching Engine |
| MockGenerativeModel | Gemini API |

---

## Production Architecture

```text
User Query
    ↓
Gemini Query Rewriter
    ↓
Vertex AI Embeddings
    ↓
Vertex AI Matching Engine
    ↓
Top-K Semantic Chunks
    ↓
LLM Response Generation
```

# 🔒 Design Principles

This project follows:

✅ Clean Architecture  
✅ Separation of Concerns  
✅ Modular Design  
✅ Production-Oriented Structure  
✅ Testability  
✅ Extensibility  

---

# 👨‍💻 Engineering Notes

This implementation was intentionally structured like a production repository rather than a prototype script.

Key focus areas:
- maintainability
- retrieval experimentation
- benchmark clarity
- enterprise migration readiness

# 🙌 Acknowledgements

- Sentence Transformers
- FAISS
- Hugging Face
- Vertex AI design inspiration

---

# ⭐ Final Result

The benchmark demonstrates that AI-enhanced query expansion improves semantic retrieval quality over traditional vector similarity search.

This validates the effectiveness of context-aware retrieval pipelines in modern RAG systems.

---
