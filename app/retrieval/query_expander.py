from app.embeddings.mocked_vertex import MockGenerativeModel

class QueryExpander:
    def __init__(self):
        self.model = MockGenerativeModel()

    def expand(self, query: str) -> str:
        return self.model.generate_content(query)