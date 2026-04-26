# LLM learning pack for regolith.pdf

This folder contains extraction output designed for later LLM reading and audit.

## Important rule

Candidate equations, tables, figures, and embedded images are **not automatically final facts**. Use `candidate_inventory.jsonl` and `extraction_review_tasks.jsonl` to classify false positives and search for false negatives.

## Files

- `llm_learning_document.json`: complete audit-ready package.
- `candidate_inventory.jsonl`: one candidate per row, with page, bbox, crop path, nearby context, and heuristic triage.
- `extraction_review_tasks.jsonl`: one page-level review task per page for false positive and false negative detection.
- `hybridrag_units_audit_ready.jsonl`: the units sent into HybridRAG.

## Candidate counts

```json
{
  "equation": 6,
  "table": 2,
  "figure": 13
}
```
