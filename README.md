# Enterprise RAG Platform

A runnable retrieval-augmented generation reference service with deterministic retrieval and explicit citations.

## Run
```bash
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

POST a query as `{"value":"incident response"}` to `/v1/run`.

## Production extensions
Add embedding retrieval, hybrid search, document ingestion, tenant-aware ACL filtering, reranking, answer generation, citation validation, and evaluation.
