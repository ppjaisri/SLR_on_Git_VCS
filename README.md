# How Researchers Construct their Dataset: An Systematic Literature Review On GitHub Repositories

<div style="text-align:justify">

## Research Questions
1. Was the dataset independently collected by the researchers, or was it derived from an existing dataset curated by others?
2. What is the most common criteria were used for dataset selection?
3. How is the dataset utilized within the scope of the paper?

## Classification Concept

The classification will contains 2 mandatory categories: Data source (RQ 1) and Filter of repository level (RQ 2)

### **RQ 1**: <ins>Most common source of dataset</ins> <br>

> <span style="color:yellow;">**Warning**</span> <br>
> Limiting the source to only GitHub maybe exclude some research paper away even the context of the paper is relate to this SLR study. <br>
> If the thrid-party dataset contains similar data with the GitHub maybe possible to included as "Derived" (Git-relavant sources).

Determine the source of the main dataset mentioned in the paper.
- *Direct*: Collect directly from GitHub either through APIs or scrapers, <span style="color:grey">~~not include~~</span> <ins><b>including</b></ins> the external Git server (ex. Gerrit Code Review, Google Andriod, etc.) and other version control provider (ex. GitLab, BitBucket, etc.). More detail, refer [VCS selection section](#Version-control-system-platform)
- *Derived*: Use 3rd party dataset that contains GitHub repository data, <span style="color:grey">~~not include~~</span> <ins><b>including</b></ins> the external Git server and other version control provider as well as "Direct" type. More detail, refer [third-party dataset section](#Third-Party-datasets)
- *Both*: Contains at least 1 "Direct" and 1 "Derived".
- *Not relavant*: Mentioned dataset does not fit into "Direct" type or hard to traceback to find the detail of mentioned dataset (further than references level 2 from Snowballing technique).
- *Not mentioned*: No detail of dataset mentioned in the paper.

### **Rq 2**: <ins>Most common criteria or filter of repositories selection</ins> <br>

Determine the criteria of filters of repositories selection.
To determine the relevant criteria in this study, the selected criteria is the criteria which mention the data that <b style="color:yellow">can be able to collect directly through GitHub for "Direct" type<sup>1</sup></b> or <b style="color:lightgreen">can be able to collect directly through the mentioned dataset for "Derived" type<sup>2</sup></b>, i.e., can be collected from API directly.
If the criteria mentioned the data or information that require the preprocessing after collecting the data from API, these criteria will be excluded from this study.

> <sup>1</sup> The data must be accessibled from the result of APIs, the preprocessing will be excluded. <br>
> <sup>2</sup> The data must be accessibled from the result of APIs and the dataset to control the field of data.

Criteria can be inherited from references.
<span style="color:teal;padding:3px;border-radius:4px"><ins>**If the criteria is refer further than references level 2, the criteria will be None**</ins></span>.
The criteria will be classified as followed:
- Quantitative criteria
- Qualitative criteria

Both of criteria will be classified into "Have", "Inherit", and "No" as the following;
- *Have*: Can be classified for all of data source.
  - For "Direct", it refers that a research paper has the criteria for repository selection.
  - For "Derived", it refers that the research paper add the criteria further than the criteria provided from the derived dataset.
  - For "Both", "Direct" and "Derived" in a research paper.
- *Inherit*: Available only category "Both". The research paper applied the repository selection criteria to the third-party dataset whether the thrid-party dataset is related to GitHub or not then extend the dataset through GitHub.
  - The third-party is related to GitHub: Fill the dataset name and detail in the extraction.
  - The third-party is not relavant to GitHub: Left the dataset field empty.
- *No*: No repository selection criteria provided in the paper for type "Derived" dataset. The type "Direct" dataset always has the criteria.

### **RQ 3**: <ins>Most common research objective</ins> <br>
Determine the goal or research objective and the purpose of used dataset or collected dataset.

#### For research goal or research objective
If the research paper introduce multiple task or proposed methodology, <span style="color:cyan"><b>only the corresponding purpose that introduce the related dataset<sup>3</sup> will be extracted</b></span>, the rest will be exlude.
For example, if a research paper contains 2 research questions and only first research question use a dataset which is related to GitHub, only purpose from first research question will be extracted while the purpose from second research question part will be excluded.

> <sup>3</sup> The related dataset is a dataset that match either "Direct", "Derive" , or "Both" type.

#### For purpose of used or collected dataset
Since a single third-party or collected dataset can be used with multiple purpose. The purpose will be classified separately and will be classified in the further step (Result of [RQ 3](#rq-3:-relationship-between-research-objective-and-selection-criteria))

### Version control system platform
The mainly focus platforms in this study must be version control system (VCS) platforms.
However, there are some platforms that similar to the VCS platforms but the core is not VCS.
The following rules are the rules for selecting the target platform
1. The repository must be a primary unit of the platform.
2. The Git removing will break the platform system.
3. The main collaboration built around fork, branch, pull requests, and review.

### Third-Party datasets
Since the third-party dataset can be constructed from multiple data sources which may be confused or feel ambiguous to distinguish.
The third-party dataset selection criteria are the following criteria:
1. If the third-party dataset is composited from multiple-data source, the dataset will be included in this study if the third-party dataset contains the data from the mainly focus VSC platforms at least 50% of entire dataset.
2. The third-party dataset must contains the data which can be collected through the VSC platform.
3. The data from third-party dataset must be related to software engineering field. Unless it will not be included in this study (eg., the third-party dataset is collected from GitHub but the data is a dataset for visualization)

## Paper Classification Gold Standard
After apply the inclusion and exclusion criteria, 147 research papers has been collected.

### Inclusion & Exclusion criteria
- Research papers must be published between 2021 and 2025 to ensure that the content of research papers are still new.
- All research papers are collected from 7 venues from top most citation venue provide by Google Scholars.
- Excluding Interviews, Survey, SLR, Tool reviews without evaluation dataset papers since these research papers are never interact with GitHub repository.

<details>
  <summary>List of the venue include in this study</summary>

  - (ICSE) International Conference on Software Engineering
  - (TSE) IEEE Transactions on Software Engineering
  - (ESEC/FSE) European Software Engineering Conference and Symposium on the Foundations of Software Engineering, -> treat as (FSE) International Symposium on Foundations of Software Engineering
  - (EMSE) Empirical Software Engineering, -> Return ESEM (Empirical Software Engineering and Measurement)
  - (ASE) International Conference on Automated Software Engineering
  - (ISSTA) International Symposium on Software Testing and Analysis
  - (MSR) Mining Software Repositories
  - (ICSME) International Conference on Software Maintenance and Evolution
</details>

### Manual Classification

> Should all dataset be extracted regardless the relationship to the Git-relavant VSC?

Classification fields, the classification file can be found at [this spreadsheet](https://docs.google.com/spreadsheets/d/133Fk_pwvJIIvWRowjzOBRJWYBnO27NaxU2iMrrTHakQ/edit?usp=sharing).
Below is the guideline for the classification

---
| **Case** | **Scenario** | **Data Source** | **Criteria of Repository Level** |
|:---:|---|:---:|:---:|
|  <b>1</b><sup><sup>  | Used dataset is collected from Git-relavant sources | <span style="background-color:darkgreen;padding:3px 32px;color:lightgreen;border-radius:4px;">Direct</span> | <span style="background-color:lightgreen;padding:3px 20px;color:darkgreen;border-radius:4px;">Have</span> |
|  <b>2</b>  | Used dataset is third-party dataset and applied the criteria to selected the target information | <span style="background-color:#0066ff;padding:3px 26px;color:#b3e6ff;border-radius:4px;">Derived</span> | <span style="background-color:lightgreen;padding:3px 20px;color:darkgreen;border-radius:4px;">Have</span> |
|  <b>3</b>  | Used a thrird-party dataset directly without applied any criteria | <span style="background-color:#0066ff;padding:3px 26px;color:#b3e6ff;border-radius:4px;">Derived</span> | <span style="background-color:#ffd6cc;padding:3px 7.5px;color:red;border-radius:4px;">Not have</span> |
|  <b>4</b>  | Used dataset include both collected from Git-relavant sources and Git-relavant third-party dataset separately | <span style="background-color:purple;padding:3px 36px;color:violet;border-radius:4px;">Both</span> | <span style="background-color:lightgreen;padding:3px 20px;color:darkgreen;border-radius:4px;">Have</span> |
|  <b>5</b>  | Used dataset is based on Git-relavant third-party dataset then extend with Git-relavant sources with additional criteria | <span style="background-color:purple;padding:3px 36px;color:violet;border-radius:4px;">Both</span> | <span style="background-color:skyblue;padding:3px 6px;color:#006699;border-radius:4px;">Internal Inherit</span> |
|  <b>6</b>  | Used dataset is derived from non Git-relavant dataset that extend the dataset with data from Git-relavant sources with additional criteria | <span style="background-color:purple;padding:3px 36px;color:violet;border-radius:4px;">Both</span> | <span style="background-color:skyblue;padding:3px 4px;color:#006699;border-radius:4px;">External Inherit</span> |
|  <b>7</b>  | The dataset is not mentioned in the research paper | <span style="background-color:grey;padding:3px;color:beige;border-radius:4px;">Not mentioned</span> | - |
|  <b>8</b>  | Used dataset is not collected from the Git-relavant source or used a third-party dataset which is not relavant to Git-relavant sources | <span style="background-color:grey;padding:3px 10px;color:beige;border-radius:4px;">Not relavant</span> | - |
---

<details>
  <summary>Terminology</summary>

  - Git-relavant sources: The version control system (VCS) like GitHub and other GitHub-like platforms, e.g., GitLab, BitBucket, Gerrit, etc.
  - Git-relavant third-party dataset: The third-party dataset which derived from Git-relavant sources.
</details>
<br>

> <b>*</b> Only if the dataset is collected through the <ins style="color:aquamarine"><b>Git-based platforms with built-in version control</b></ins> (i.e., a platform where VCS is the core purpose) will be classified as <span style="background-color:darkgreen;padding:3px 32px;color:lightgreen;border-radius:4px;">Direct</span> <br>
> Example of VCS-as-core platform: GitHub, GitLab, BitBucket <br>
> Some platforms has integrated Git system by VCS is not a core: Hugging Face, Zenodo

<br>

**Use GitHub Dataset (Data source)**: The sources of dataset which can be classified into 5 types Direct, Derived, Both, Not relavant, and Not mentioned. If it is classified as "Not relavant" or "Not mentioned", the rest of classification will be skipped. <br>

**Repository Criteria Level**: If the paper describe the criteria for repositoy level selection, will be classified as "Have". Will be classified as "internal inherit" if the paper leverage the criteria from the Git-relavant third-party dataset, but if the paper apply the criteria from the non-GitHub third-party dataset, it will be classified as "external inherit". Otherwise will be classified as "Not have". <br>

**Quantitative & Qualitative Criteria**: The filter or criteria to select the repository. It will be a list of the filter or criteria at repository level.
  <!-- - *Repository level*: The filter or criteria that refer to repository perspective selection. -->
  <!-- - *Post repository level*: The filter or criteria that refer to other perspective selection. -->
**Dataset**: The dataset informations.
- *Name*: The name of the dataset.
- *Detail*: The detail of the dataset, what is included in the dataset.
- *Purpose*: The purpose of dataset usage in the paper if there are multiple datasets or data sources.
<!-- - *Limitations*: The limitation of the dataset, if the paper mention it. -->
**External Dataset**: The non-Git-relavant dataset name.
**Purpose**: The purpose or objective of the research paper.

### LLMs Classification
Use ChatGPT 5.2 through Open-Router APIs to classify the 147 sample papers.

### Evaluation
Use Cohen's Kappa score to measure the agreement between ChatGPT and Human

## Results

### RQ 1: Most common source of dataset
Most common source (from 146 sample papers)
- Direct: - papers
- Derived: - papers
- Both: - papers
- Not relavant: - papers
- Not mentioned: - papers

Purpose of third-party dataset used in the experiment (from 146 sample papers)
1. Empirical study: - dataset -> Dataset A, B, C ,...
2. Evaluation: - dataset -> Dataset A, B, C ,...
3. ...

Most popular third-party dataset
1. ...
2. 
3. 

### RQ 2: Most common repository selection criteria

Most common quantitative criteria
1. criteria A
2. ...
3. 

Most common qualitative criteria
1. criteria B
2. ...
3. 

### RQ 3: Relationship between research objective and selection criteria

Most common research objective (from 146 sample papers)
- Evaluation: - papers
- Framework / tool proposing: - papers
- Empirical study: - papers
- ...

<div>