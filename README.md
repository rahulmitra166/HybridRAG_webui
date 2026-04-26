# HybridRAG OpenAI Notebook

This package contains an OpenAI-backed version of the HybridRAG notebook.

## Files

- `HybridRAG_OpenAI.ipynb` — main notebook.
- `pdf_to_llm_open_source.py` — local PDF extraction module used by the notebook.
- `requirements_openai_hybridrag.txt` — Python packages.

## Setup

```bash
pip install -r requirements_openai_hybridrag.txt
export OPENAI_API_KEY="sk-..."
```

Put PDFs in `myPDFs/`, then run the notebook from top to bottom.

## Default models

- LLM: `gpt-5.2`
- Embeddings: `text-embedding-3-large`

Override with environment variables:

```bash
export OPENAI_GENERATION_MODEL="gpt-5.2"
export OPENAI_ANSWER_MODEL="gpt-5.2"
export OPENAI_EMBEDDING_MODEL="text-embedding-3-large"
export OPENAI_REASONING_EFFORT="medium"
```

For faster/cheaper runs, use lower reasoning effort or a smaller model:

```bash
export OPENAI_REASONING_EFFORT="none"
export OPENAI_GENERATION_MODEL="gpt-5-mini"
export OPENAI_ANSWER_MODEL="gpt-5-mini"
export OPENAI_EMBEDDING_MODEL="text-embedding-3-small"
```

The notebook writes output to `rag_output_openai/` by default so it does not collide with older local/Ollama vector stores.
