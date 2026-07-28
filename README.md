# Replication Package

Replication package for the paper *Show me the Dataset! Preliminary Exploration into Empirical Software Engineering
Research*, a systematic mapping study of empirical software engineering research published in ten major SE venues between 2021 and 2025.

> **Note on scope.** This README documents the replication of the **empirical-study characterization** reported in the paper: analysis type (RQ1), research topic (RQ2), and dataset contribution (RQ3). The classification in that paper is performed **manually**.

---

## 1. What this package contains

| Path | Description |
| --- | --- |
| `systematic_literature_review.ipynb` | The full pipeline: paper collection, screening, DOI validation, abstract retrieval, and corpus statistics. |
| `pyproject.toml` | Python dependencies and environment definition (Poetry). |
| `data/` | All intermediate and final data files (see §4). **Currently excluded by `.gitignore` — see §6.** |
| `README.md` | This file. |

---

## 2. Requirements

- **Python ≥ 3.12**
- **[Poetry](https://python-poetry.org/) ≥ 2.0**
- A **Semantic Scholar API key** ([request one here](https://www.semanticscholar.org/product/api#api-key-form)). The pipeline works without a key but is heavily rate-limited.
- Network access to `api.semanticscholar.org` and `citation.doi.org`.

Runtime for a full re-run is dominated by API calls; expect **several hours** for the ~9,400-paper collection step, mostly spent waiting on rate limits.

---

## 3. Setup

```bash
git clone https://github.com/ppjaisri/SLR_on_Git_VCS.git
cd SLR_on_Git_VCS

# install dependencies (including the dev group, needed for the notebook)
poetry install --with dev

# register the kernel and open the notebook
poetry run python -m ipykernel install --user --name slr-on-git-vcs
poetry run jupyter lab systematic_literature_review.ipynb
```

Create a `config.py` in the repository root for your credentials (this file is git-ignored):

```python
SEMANTIC_SCHOLAR_API_KEY = "your-key-here"
```

---

## 4. Pipeline

Run the notebook cells in order. Each stage reads the previous stage's output and writes a new JSONL file under `data/`, so a stage can be re-run without repeating the ones before it.

| # | Stage | Input | Output | Papers remaining |
| --- | --- | --- | --- | ---: |
| 1 | Collect paper metadata per venue from the Semantic Scholar API | — | `data/semantic_data/*.jsonl` | 9,428 |
| 2 | Screen titles: English, valid length, non-editorial, non-secondary | `data/semantic_data/*.jsonl` | `data/filtered_papers_by_title.jsonl` | 8,183 |
| 3 | Normalize venue-name variants | ↑ | `data/filtered_papers_by_title_with_venue_variants.jsonl` | 8,183 |
| 4 | Retain papers self-identifying as empirical (title keyword match) | ↑ | `data/filter_empirical_study.jsonl` | 447 |
| 5 | Retrieve abstracts from the Semantic Scholar API | ↑ | `data/empirical_papers_with_abstract.jsonl` | 202 |
| 6 | Manual classification along D1–D3 | ↑ | `data/classified_papers.csv` | 202 |

Stage 7 is **not automated**: the labels are produced by human inspection of each paper's title and abstract (and full text where these are insufficient). The completed annotation file is what the analysis in §5 consumes.

> **Reproducibility caveat.** Stages 1 and 6 query a live API, so re-running them at a later date may return slightly different results as Semantic Scholar's index changes. To reproduce the exact numbers in the paper, use the archived `data/` snapshot rather than re-collecting.

---

## 5. Reproducing the results in the paper

| Paper artifact | Produced by |
| --- | --- |
| Table 1 — Corpus construction per venue | Notebook cells reporting counts per stage (§4) |
| Table 2 — Selected publication venues | Static; bibliometric values retrieved manually |
| Table 3 — CCS category ↔ `key_id` mapping | Static; see the classification codebook |
| Table 4 — Analysis type per venue | `data/classified_papers.csv`, grouped by venue × D1 |
| Table 5 — Research topic distribution | `data/classified_papers.csv`, grouped by D2 |
| Table 6 — Dataset contribution per venue | `data/classified_papers.csv`, grouped by venue × D3 |
| Figure 1 — Study methodology overview | Drawn in LaTeX (TikZ); not generated from data |

<!-- TODO: adjust table numbers if the manuscript is reordered. -->

### Classification codebook

Each paper is labeled along three dimensions:

- **D1 — Analysis type:** `quantitative`, `qualitative`, or `both`.
- **D2 — Research topic:** one of 18 categories derived from the ACM Computing Classification System. Categories accounting for < 1% of the corpus are merged into `other_se` **for reporting only**.
- **D3 — Dataset contribution:** binary; counted only when a newly constructed dataset is explicitly mentioned in the title or abstract.

<!-- TODO: export the full category definitions and decision rules here or as
     data/codebook.md, so that the labels can be independently reproduced. -->

---

## 6. Known limitations of this package

These are open items rather than instructions — please read before attempting a replication.

1. **The `data/` directory is currently git-ignored, so no data ships with this repository.** Without it, none of §4 or §5 can be reproduced. Either remove `data` from `.gitignore` (if file sizes permit) or archive the directory on Zenodo/figshare and link the DOI here.
2. **The notebook contains hard-coded absolute paths** (e.g. `/Users/ppjaisri/Coding/phd/SLR_on_Git_VCS/data/...`). Replace these with paths relative to the repository root.
3. **`matplotlib` and `numpy` are imported by the notebook but are not declared in `pyproject.toml`.** Add them to the dev dependency group.
4. **The manual annotations are maintained in an external spreadsheet.** Export them into `data/` so the package is self-contained.

---

## 7. Citation

```bibtex
@inproceedings{pongchaiSLR,
  author    = {Pongchai Jaisri, Youmei Fan, Raula Gaikovina Kula, Kenichi Matsumoto},
  title     = {Show me the Dataset! Preliminary Exploration into Empirical Software Engineering Research},
  journal   = {Journal of Information Processing}
  year      = {2026}
}
```

## 8. License

Code is released under the MIT License (see `pyproject.toml`). Paper metadata retrieved from Semantic Scholar and Crossref remains subject to those providers' terms.