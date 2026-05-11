from app.retrieval.query_expander import QueryExpander

class Retriever:
    def __init__(self, embedding_model, vector_store):
        self.embedding_model = embedding_model
        self.vector_store = vector_store
        self.expander = QueryExpander()

    def retrieve_raw(self, query: str):
        embedding = self.embedding_model.embed([query])

        return self.vector_store.search(embedding)

    def retrieve_expanded(self, query: str):
        expanded_query = self.expander.expand(query)

        embedding = self.embedding_model.embed([expanded_query])

        results = self.vector_store.search(embedding)

        return expanded_query, results