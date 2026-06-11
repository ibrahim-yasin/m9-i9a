# Integration 9A — Query Suite Notes

Fill in one section per query (Q1–Q8) with:
- **Intent:** one sentence stating what the query answers in business terms.
- **Result:** the first 5 rows (or triple count for CONSTRUCT, boolean for ASK).

Use the template below.

---

## Q1 — Authors at NeurIPS

**Intent:** Lists all authors who have published at least one paper in the NeurIPS venue.

**Result (first 5 rows):**

| author |
|----------|
| http://aispire.example.org/publications/author000 |
| http://aispire.example.org/publications/author001 |
| http://aispire.example.org/publications/author100 |
| http://aispire.example.org/publications/author004 |
| http://aispire.example.org/publications/author111 |

## Q2 — Papers per topic

**Intent:** Counts how many papers are associated with each research topic.

**Result (first 5 rows):**

| topic | n |
|--------|---|
| topic_interpretability | 2 |
| topic_summarization | 3 |
| topic_recommender-systems | 2 |
| topic_self-supervised | 5 |
| topic_attention | 1 |

## Q3 — Canonical coauthor pairs

**Intent:** Lists all unique coauthor pairs who have collaborated on at least one paper, with each pair shown only once in canonical order.

**Result (first 5 rows):**

| a | b |
|---|---|
| author000 | author001 |
| author000 | author100 |
| author000 | author004 |
| author000 | author111 |
| author000 | author039 |

## Q4 — Papers and DOIs

**Intent:** Lists all papers and their DOI values, while still including papers that do not have a DOI assigned.

**Result (first 5 rows):**

| paper | doi |
|--------|--------|
| paper000 | 10.1000/p000 |
| paper001 | (unbound) |
| paper002 | (unbound) |
| paper003 | 10.1000/p003 |
| paper004 | (unbound) |

## Q5 — Prolific authors (ASK)

**Intent:** Checks whether there exists at least one author who has published more than 10 papers in the dataset.

**Result:** True

## Q6 — 2023 papers with authors (CONSTRUCT)

**Intent:** Constructs a graph linking all papers published in 2023 to their authors using the :authoredBy relationship.

**Result:** 31 triples emitted.

## Q7 — Top 5 most-cited

**Intent:** Identifies the five papers with the highest citation counts in the dataset.

**Result (top 5 rows):**

| paper | citationCount |
|--------|--------|
| paper063 | 485 |
| paper043 | 475 |
| paper004 | 473 |
| paper007 | 470 |
| paper048 | 470 |

## Q8 — "Hinton" via SKOS

**Intent:** Finds authors whose name matches the term "Hinton" through either a SKOS preferred label (`skos:prefLabel`) or an alternative label (`skos:altLabel`), demonstrating ontology-based disambiguation.

**Result:**

| author | matched label |
|---------|---------|
| author000 | "Hinton" (prefLabel or altLabel) |
| author007 | "Hinton" (prefLabel or altLabel) |
###
