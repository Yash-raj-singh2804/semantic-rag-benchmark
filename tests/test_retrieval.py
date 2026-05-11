from app.retrieval.query_expander import QueryExpander

def test_query_expansion():
    expander = QueryExpander()

    expanded = expander.expand(
        "How does the system handle peak load?"
    )

    assert "autoscaling" in expanded