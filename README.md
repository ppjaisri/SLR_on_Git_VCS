# SLR on Git VCS

This repository contains a systematic literature review workflow for studying Git and related version-control research in software engineering. The project combines metadata collection, title and abstract screening, empirical paper filtering, and manual/LLM-assisted classification of research themes and dataset contribution.

The notebook pipeline focuses on building a reproducible evidence base for Git/VCS-related software engineering studies and classifying the resulting papers according to their empirical characteristics.

---

## 1. Repository contents

| Path                                        | Description                                                               |
| ------------------------------------------- | ------------------------------------------------------------------------- |
| `systematic_literature_review.ipynb`        | Main analysis notebook for the SLR pipeline and paper filtering workflow. |
| `systematic_literature_review_backup.ipynb` | Backup copy of the notebook used during earlier exploratory work.         |
| `analysis_types_keywords_list.json`         | Keyword list used for categorization and filtering.                       |
| `llm_prompt.txt`                            | Prompt used for LLM-based classification of paper abstracts.              |
| `llm_prompt_json_schema.json`               | JSON schema constraining the LLM output format.                           |
| `Manual Classification.csv`                 | Manual annotation file for classified papers.                             |
| `pyproject.toml`                            | Poetry project definition and Python dependencies.                        |
| `data/`                                     | Intermediate and final paper datasets (JSONL/CSV outputs).                |
| `README.md`                                 | Repository overview and setup notes.                                      |

---

## 2. Project goal

The project explores the literature around Git and version-control systems as a research topic in software engineering. In practice, the workflow is structured as follows:

1. Collect candidate papers from academic venues and metadata sources.
2. Filter out irrelevant or non-eligible papers by title and metadata.
3. Keep only papers that appear to be empirical software engineering studies.
4. Retrieve abstracts and classify their properties.
5. Label analysis type, research topic, and dataset contribution.
6. Prepare the resulting corpus for downstream analysis and reporting.

---

## 3. Requirements

- Python 3.12+
- Poetry 2.0+
- Internet access for metadata retrieval and abstract lookups
- Optional: Semantic Scholar API key for higher throughput and fewer rate limits

The project may also require a few scientific Python packages in the notebook environment, including `numpy`, `pandas`, and `matplotlib`.

---

## 4. Setup

```bash
git clone https://github.com/ppjaisri/SLR_on_Git_VCS.git
cd SLR_on_Git_VCS

poetry install --with dev
poetry add --group dev numpy pandas matplotlib ipykernel

poetry run python -m ipykernel install --user --name slr-on-git-vcs
poetry run jupyter lab systematic_literature_review.ipynb
```

If you use a Semantic Scholar API key, create a local config file such as:

```python
SEMANTIC_SCHOLAR_API_KEY = "your-key-here"
```

This file is typically kept outside version control and can be used by the notebook if needed.

---

## 5. Typical workflow

The notebook is generally run in order, with each stage reading the previous stage's outputs and writing new files under `data/`.

| Stage | Purpose                                         | Typical output                                            |
| ----- | ----------------------------------------------- | --------------------------------------------------------- |
| 1     | Collect metadata for candidate papers           | `data/semantic_data/*.jsonl`                              |
| 2     | Title-based screening                           | `data/filtered_papers_by_title.jsonl`                     |
| 3     | Venue normalization / deduplication             | `data/filtered_papers_by_title_with_venue_variants.jsonl` |
| 4     | Empirical-study filtering                       | `data/filter_empirical_study.jsonl`                       |
| 5     | Abstract retrieval                              | `data/empirical_papers_with_abstract.jsonl`               |
| 6     | Manual or structured classification             | `data/*.csv` / `data/*.jsonl`                             |
| 7     | LLM-based classification of the selected papers | `data/llm_classified_papers.jsonl`                        |

---

## 6. Data notes

The project stores intermediate and final data under `data/`. Depending on the stage, the files include:

- candidate paper metadata
- filtered title lists
- empirical-study subsets
- abstract-enriched paper records
- manual classification outputs
- LLM-assisted classification outputs

> The repository currently expects a local `data/` directory to exist. Some outputs may be excluded from Git depending on repository configuration or dataset size.

---

## 7. Known caveats

This project is a research notebook rather than a packaged software application, so a few practical limitations remain:

1. Several notebook cells use hard-coded local file paths and are not fully portable across machines.
2. Some stages depend on live external APIs, so re-running them may produce slightly different results over time.
3. The notebook imports scientific Python libraries that should be present in the environment, even if they are not fully declared in the current `pyproject.toml`.
4. Manual and scripted classification outputs are stored in repository data files and may need to be synchronized with the notebook outputs.

---

## 8. License

This project is released under the MIT license, as specified in `pyproject.toml`.

---

## 9. Research usage

This repository is intended to support a reproducible systematic review workflow for Git/VCS-related software engineering research. It is best used as a data collection and classification pipeline for study replication, corpus preparation, and literature analysis.
