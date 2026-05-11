class MockTextEmbeddingModel:
    @classmethod
    def from_pretrained(cls, name: str):
        return cls()

    def get_embeddings(self, texts):
        return texts

class MockGenerativeModel:
    def generate_content(self, prompt: str):
        expansions = {
            "peak load":
                "system scalability autoscaling traffic spikes throughput balancing",
            "database failure":
                "database redundancy failover recovery replication resilience",
            "latency":
                "latency optimization caching CDN edge routing performance bottlenecks response time"
        }

        expanded_query = prompt

        for key, value in expansions.items():
            if key in prompt.lower():
                expanded_query += " " + value

        return expanded_query