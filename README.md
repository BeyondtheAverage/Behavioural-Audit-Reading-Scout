# Behavioural-Audit-Reading-Scout

## Goal: Find recent papers and articles about AI reliability, evaluation, agent behaviour and assurance, then produce:

* outputs/reading_list.csv
* outputs/weekly_brief.md (written by your local LM Studio model)

## Data sources (APIs)

Start with Semantic Scholar (clean JSON, good metadata). Optional later:

* arXiv (preprints)
* GDELT (news)

## Local LLM

LM Studio running an OpenAI-compatible server at something like:
http://localhost:1234/v1

## A simple LangGraph pipeline:

### QueryBuilder
Takes your topic like “behavioural audit reliability of LLMs” and expands into 3–6 search queries.

### FetchSemanticScholar
Calls the Semantic Scholar search API for each query and returns candidates.

### CleanRankDedup
Deduplicates, ranks by recency + citations + keyword match, picks top N.

### BriefWriter (LM Studio)
Your local model writes a one-page “weekly brief” from the ranked list.

Export
Writes CSV + Markdown.
