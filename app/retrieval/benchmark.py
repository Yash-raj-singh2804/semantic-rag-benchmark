from app.models.schemas import BenchmarkResult

class BenchmarkRunner:
    def __init__(self, retriever):
        self.retriever = retriever

    def run(self, queries):
        benchmark_results = []

        for query in queries:

            strategy_a = self.retriever.retrieve_raw(query)

            expanded_query, strategy_b = (
                self.retriever.retrieve_expanded(query)
            )

            benchmark_results.append(
                BenchmarkResult(
                    query=query,
                    expanded_query=expanded_query,
                    strategy_a_results=strategy_a,
                    strategy_b_results=strategy_b
                )
            )

        return benchmark_results