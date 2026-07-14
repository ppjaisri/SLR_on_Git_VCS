# How Researchers Construct Their Dataset: A Systematic Literature Review on GitHub Repositories

## Research Questions
1. Was the dataset independently collected by the researchers, or was it derived from an existing dataset curated by others?
2. What are the most common criteria used for dataset selection?
3. How is the dataset utilized within the scope of the paper?

## Study Scope and Definitions

This section defines the platforms and datasets considered in this study. These definitions are used throughout the classification.

### Version control system platform
The platforms mainly focused on in this study must be version control system (VCS) platforms.
However, some platforms are similar to VCS platforms, but their core is not VCS.
The following rules are used for selecting the target platforms:
1. The repository must be a primary unit of the platform.
2. Removing Git would break the platform system.
3. The main collaboration is built around forks, branches, pull requests, and reviews.

### Third-party datasets
Since a third-party dataset can be constructed from multiple data sources, it may be confusing or ambiguous to distinguish.
The third-party dataset selection criteria are the following:
1. If the third-party dataset is composed of multiple data sources, it will be included in this study if it contains data from the mainly focused VCS platforms.
<!-- for at least 50% of the entire dataset. -->
2. The third-party dataset must contain data which can be collected through the VCS platform.
3. The data from the third-party dataset must be related to the software engineering field; otherwise, it will not be included in this study (e.g., the third-party dataset is collected from GitHub but the data is a dataset for visualization).

### Terminology
- **Git-relevant sources**: Version control system (VCS) platforms that built-in with Git system like GitHub and other GitHub-like platforms, e.g., GitLab, Bitbucket, Gerrit, etc.
- **Git-relevant third-party dataset**: A third-party dataset derived from Git-relevant sources.

## Paper Collection
After applying the inclusion and exclusion criteria, 370 research papers have been collected as the gold standard.

### Inclusion & exclusion criteria
- Research papers must be published between 2021 and 2025 to ensure that the content of the research papers is still recent.
- All research papers are collected from 10 venues, based on the most-cited venues provided by [Google Scholar](https://scholar.google.com/citations?view_op=top_venues&hl=en&vq=eng_softwaresystems).
- Interviews, surveys, SLRs, and tool reviews without an evaluation dataset are excluded, since these research papers never interact with GitHub repositories.

<details>
  <summary>List of the venues included in this study</summary>

  - (ICSE)  International Conference on Software Engineering
  - (TSE)   IEEE Transactions on Software Engineering
  - (TOSEM) ACM Transactions on Software Engineering and Methodology
  - (EMSE)  Empirical Software Engineering
  - (JSS)   Journal of Systems and Software
  - (FSE)   International Conference on the Foundations of Software Engineering
  - (ASE)   International Conference on Automated Software Engineering
  - (MSR)   International Conference on Mining Software Repositories
  - (ICSME) International Conference on Software Maintenance and Evolution
  - (SANER) International Conference on Software Analysis, Evolution and Reengineering
</details>

## Classification Concept

The classification contains 2 mandatory categories: Data source (RQ 1) and Repository-level filter (RQ 2).

### **RQ 1**: <ins>Most common source of dataset</ins>

<!-- > [!WARNING]
> Limiting the source to only GitHub may exclude some research papers even when the context of the paper is related to this SLR study. <br>
> If a third-party dataset contains data similar to GitHub, it may be possible to include it as "Derived" (Git-relevant sources). -->

Determine the source of the main dataset mentioned in the paper.
- *Direct*: Collected directly from GitHub either through APIs or scrapers, **including** external Git servers (e.g., Gerrit Code Review, Google Android, etc.) and other version control providers (e.g., GitLab, Bitbucket, etc.). For more detail, refer to the [VCS selection section](#version-control-system-platform).
- *Derived*: Uses a third-party dataset that contains GitHub repository data, **including** external Git servers and other version control providers, as in the "Direct" type. For more detail, refer to the [third-party dataset section](#third-party-datasets).
- *Both*: Contains at least 1 "Direct" and 1 "Derived" source.
- *Not relevant*: The mentioned dataset does not fit into the "Direct" type, or it is hard to trace back the detail of the mentioned dataset (further than reference level 2 from the snowballing technique).
- *Not mentioned*: No detail of the dataset is mentioned in the paper.

### **RQ 2**: <ins>Most common criteria or filters for repository selection</ins>

Determine the criteria or filters for repository selection.
To determine the relevant criteria in this study, a selected criterion is one that mentions data that <b style="color:yellow">can be collected directly through the VCS platform for the "Direct" type<sup>1</sup></b> or <b style="color:lightgreen">can be collected directly through the mentioned dataset for the "Derived" type<sup>2</sup></b>, i.e., can be collected from the platform's API directly.
If a criterion mentions data or information that requires preprocessing after collecting the data from the API, it will be excluded from this study.

> <sup>1</sup> The data must be accessible from the results of the platform's APIs; preprocessing will be excluded. <br>
> <sup>2</sup> The data must be accessible from the results of the APIs and the dataset, to control the field of data.

Criteria can be inherited from references.
<span style="color:teal;padding:3px;border-radius:4px"><ins>**If a criterion is referred to further than reference level 2, the criterion will be None**</ins></span>.
The criteria will be classified as follows:
- Quantitative criteria: For example, No. GitHub instances (issues, pull requests, commits), No. contributors, etc.
- Qualitative criteria: For example, Tech-stack used in the project (Java, Python, etc.), Specific file requirement, etc.

Both types of criteria will be classified into "Have", "Inherit", and "Not have" as follows:
- *Have*: Can be classified for all data sources.
  - For "Direct", it means the research paper has criteria for repository selection.
  - For "Derived", it means the research paper adds criteria beyond those provided by the derived dataset.
  - For "Both", both "Direct" and "Derived" apply in a research paper.
- *Inherit*: Available only for the "Both" category. The research paper applied the repository selection criteria of a third-party dataset — whether the third-party dataset is Git-relevant or not — and then extended the dataset through the VCS platform.
  - The third-party dataset is Git-relevant: fill in the dataset name and detail in the extraction.
  - The third-party dataset is not Git-relevant: leave the dataset field empty.
- *Not have*: No repository selection criteria are provided in the paper for the "Derived" dataset type. The "Direct" dataset type always has criteria.

### **RQ 3**: <ins>Most common research objective</ins>

Determine the goal or research objective and the purpose of the used or collected dataset.

#### For research goal or research objective
If a research paper introduces multiple tasks or proposed methodologies, <span style="color:cyan"><b>only the corresponding purpose that introduces the related dataset<sup>3</sup> will be extracted</b></span>; the rest will be excluded.
For example, if a research paper contains 2 research questions and only the first research question uses a dataset related to a Git-relevant source, only the purpose from the first research question will be extracted, while the purpose from the second research question will be excluded.

> <sup>3</sup> A related dataset is a dataset that matches either the "Direct", "Derived", or "Both" type.

#### For purpose of the used or collected dataset
Since a single third-party or collected dataset can be used for multiple purposes, the purposes will be classified separately and refined in a further step (see the results of [RQ 3](#rq-3-relationship-between-research-objective-and-selection-criteria)).

## Paper Classification

### Manual Classification

<!-- > Should all datasets be extracted regardless of their relationship to the Git-relevant VCS? -->

The classification fields and the classification file can be found in [this spreadsheet](https://docs.google.com/spreadsheets/d/1AcT5BAufuThJSzbJTlFJKGa9ZHNSxJvQO6t4CUIKxqs/edit?usp=sharing).
Below is the guideline for the classification.

---
| **Case** | **Scenario** | **Data Source** | **Criteria of Repository Level** |
|:---:|---|:---:|:---:|
|  <b>1</b><sup>*</sup>  | The used dataset is collected from Git-relevant sources | <span style="background-color:darkgreen;padding:3px 32px;color:lightgreen;border-radius:4px;">Direct</span> | <span style="background-color:lightgreen;padding:3px 20px;color:darkgreen;border-radius:4px;">Have</span> |
|  <b>2</b>  | The used dataset is a third-party dataset, and criteria were applied to select the target information | <span style="background-color:#0066ff;padding:3px 26px;color:#b3e6ff;border-radius:4px;">Derived</span> | <span style="background-color:lightgreen;padding:3px 20px;color:darkgreen;border-radius:4px;">Have</span> |
|  <b>3</b>  | A third-party dataset is used directly without applying any criteria | <span style="background-color:#0066ff;padding:3px 26px;color:#b3e6ff;border-radius:4px;">Derived</span> | <span style="background-color:#ffd6cc;padding:3px 7.5px;color:red;border-radius:4px;">Not have</span> |
|  <b>4</b>  | The used dataset includes both data collected from Git-relevant sources and a Git-relevant third-party dataset, separately | <span style="background-color:purple;padding:3px 36px;color:violet;border-radius:4px;">Both</span> | <span style="background-color:lightgreen;padding:3px 20px;color:darkgreen;border-radius:4px;">Have</span> |
|  <b>5</b>  | The used dataset is based on a Git-relevant third-party dataset, then extended with Git-relevant sources with additional criteria | <span style="background-color:purple;padding:3px 36px;color:violet;border-radius:4px;">Both</span> | <span style="background-color:skyblue;padding:3px 6px;color:#006699;border-radius:4px;">Internal Inherit</span> |
|  <b>6</b>  | The used dataset is derived from a non-Git-relevant dataset, then extended with data from Git-relevant sources with additional criteria | <span style="background-color:purple;padding:3px 36px;color:violet;border-radius:4px;">Both</span> | <span style="background-color:skyblue;padding:3px 4px;color:#006699;border-radius:4px;">External Inherit</span> |
|  <b>7</b>  | The dataset is not mentioned in the research paper | <span style="background-color:grey;padding:3px;color:beige;border-radius:4px;">Not mentioned</span> | - |
|  <b>8</b>  | The used dataset is not collected from Git-relevant sources, or a third-party dataset that is not relevant to Git-relevant sources is used | <span style="background-color:grey;padding:3px 10px;color:beige;border-radius:4px;">Not relevant</span> | - |
---

> <b>*</b> Only if the dataset is collected through <ins style="color:aquamarine"><b>Git-based platforms with built-in version control</b></ins> (i.e., a platform where VCS is the core purpose) will it be classified as <span style="background-color:darkgreen;padding:3px 32px;color:lightgreen;border-radius:4px;">Direct</span>. <br>
> Examples of VCS-as-core platforms: GitHub, GitLab, Bitbucket <br>
> Some platforms have an integrated Git system, but VCS is not their core: Hugging Face, Zenodo

<br>

The classification fields are described as follows:

**Use GitHub Dataset (Data source)**: The source of the dataset, which can be classified into 5 types: Direct, Derived, Both, Not relevant, and Not mentioned. If it is classified as "Not relevant" or "Not mentioned", the rest of the classification will be skipped.

**Repository Criteria Level**: If the paper describes criteria for repository-level selection, it will be classified as "Have". It will be classified as "Internal inherit" if the paper leverages the criteria from a Git-relevant third-party dataset; if the paper applies the criteria from a non-Git-relevant third-party dataset, it will be classified as "External inherit". Otherwise, it will be classified as "Not have".

**Quantitative & Qualitative Criteria**: The filters or criteria used to select repositories. This will be a list of filters or criteria at the repository level.
  <!-- - *Repository level*: The filter or criteria that refer to repository perspective selection. -->
  <!-- - *Post repository level*: The filter or criteria that refer to other perspective selection. -->

**Dataset**: The dataset information.
- *Name*: The name of the dataset.
- *Detail*: The detail of the dataset — what is included in the dataset.
- *Purpose*: The purpose of the dataset usage in the paper, if there are multiple datasets or data sources.
<!-- - *Limitations*: The limitation of the dataset, if the paper mention it. -->

**External Dataset**: The non-Git-relevant dataset name.

**Purpose**: The purpose or objective of the research paper.

### LLM Classification
Use GPT-5.2 through the OpenRouter API to classify the 147 sample papers.

### Evaluation
Use Cohen's kappa score to measure the agreement between the LLM and the human annotator.

<!-- Will be updated later -->
<!-- ## Results

### RQ 1: Most common source of dataset
Most common source (from 147 sample papers)
- Direct: - papers
- Derived: - papers
- Both: - papers
- Not relevant: - papers
- Not mentioned: - papers

Purpose of third-party datasets used in the experiments (from 147 sample papers)
1. Empirical study: - datasets -> Dataset A, B, C, ...
2. Evaluation: - datasets -> Dataset A, B, C, ...
3. ...

Most popular third-party datasets
1. ...
2. 
3. 

### RQ 2: Most common repository selection criteria

Most common quantitative criteria
1. Criteria A
2. ...
3. 

Most common qualitative criteria
1. Criteria B
2. ...
3. 

### RQ 3: Relationship between research objective and selection criteria

Most common research objective (from 147 sample papers)
- Evaluation: - papers
- Framework / tool proposing: - papers
- Empirical study: - papers
- ... -->
