class Service:
    def run(self, value: str):
        docs = [
            ("doc-1", "Enterprise agent runbooks and policies"),
            ("doc-2", "Service ownership and incident response"),
        ]
        query = set(value.lower().split())
        ranked = sorted(
            docs,
            key=lambda d: len(query & set(d[1].lower().split())),
            reverse=True,
        )
        return {
            "query": value,
            "results": [
                {
                    "id": doc_id,
                    "text": text,
                    "score": len(query & set(text.lower().split())),
                    "citation": f"{doc_id}#content",
                }
                for doc_id, text in ranked
            ],
        }
