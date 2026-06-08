import requests
import json

from pathlib import Path
from time import sleep


class Snowballing:
    def __init__(self, api_key: str, paper_pool: list[dict]):
        """_summary_

        Args:
            api_key (str): The API key for accessing the Semantic Scholar API
            paper_pool (list[dict]): A list of papers to start the snowballing process with. Each paper should be a dictionary with at least "title" and "doi" keys.
        """
        self.api_key = api_key
        # ! Mandatory Format -> {"title": str, "doi": str}
        self.paper_pool = paper_pool

    def extract_paper_citation_and_references_info(
        self,
        api_key: str,
        doi: str
    ) -> dict | None:

        headers = {
            'X-API-Key': api_key
        }

        # ? based information
        based_url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}/citations"

        params = {
            'fields': 'title,referenceCount,venue,externalIds,year'
        }

        response = requests.get(based_url, headers=headers, params=params)

        if response.status_code == 200:
            result = response.json()
            data = result['data']

            res = []
            for item in data:
                res.append({
                    'doi': item['citingPaper']['externalIds'].get('DOI', None),
                    'title': item['citingPaper'].get('title'),
                    'venue': item['citingPaper'].get('venue', None),
                    'reference_count': item['citingPaper'].get('referenceCount', 0),
                    'year': item['citingPaper'].get('year', None)
                })

            return res

        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    def fetch_citations_recursive(
        self,
        seed_ids: list[dict],
        api_key: str,
        save_path: Path,
        min_year: int = 2021,
        paper_index: int = 1,
        previous_index: int = 0,
        paper_name: str = None,
        max_level: int = 2
    ) -> int:
        # State Management
        # Papers to fetch
        queue = [{**paper, "level": paper.get("level", 0)}
                 for paper in seed_ids]
        processed_dois = set()   # Papers already fetched
        results = {}            # Final Graph: {id: {metadata, refs}}
        number_of_papers = 0

        while queue:
            # print(json.dumps(queue, indent=4, ensure_ascii=False))
            current_paper = queue.pop(0)
            # print(json.dumps(current_paper, indent=4, ensure_ascii=False))
            current_doi = current_paper.get("doi", None)
            current_title = current_paper.get("title", None)
            current_year = current_paper.get("year", None)
            current_level = current_paper.get("level", 0)

            if paper_index == 1 and paper_name is None:
                # Use first paper's title as filename (truncated and sanitized)
                paper_name = current_title.replace('/', '_')

            if current_doi in processed_dois or current_doi is None:
                continue

            # Define which fields we need (to minimize data transfer)
            # fields = "title,year,references.paperId,references.year"
            # url = f"{BASE_URL}{current_doi}?fields={fields}"

            try:
                processed_dois.add(current_doi)

                # Store data
                results[current_doi] = {
                    "title": current_title,
                    "year": current_year,
                    "references": []
                }

                # Process the children (References)
                references = self.extract_paper_citation_and_references_info(
                    api_key=api_key,
                    doi=current_doi
                )
                for ref in references:
                    ref_doi = ref.get("doi")
                    ref_year = ref.get("year")

                    if ref_doi:
                        results[current_doi]["references"].append(ref_doi)

                        with open(save_path.joinpath(current_title.replace('/', '_').replace(':', '_') + '.jsonl'), 'a+') as f:
                            json_res = json.dumps(ref, ensure_ascii=False)
                            f.write(json_res + '\n')

                        # RECURSIVE CONDITION:
                        # 1. Not already processed
                        # 2. Not already in queue
                        # 3. Paper is between 2021 and 2025
                        # 4. Main language is English (Check from title - if it contains non-English characters, we can skip it)
                        if ref_doi not in processed_dois and ref not in queue:
                            is_english = all(
                                ord(char) < 128 for char in ref.get("title", ""))
                            if current_level < max_level and min_year <= ref_year <= 2025 and is_english:
                                ref["level"] = current_level + 1
                                queue.append(ref)

                if paper_index != previous_index:
                    print(f"Index: {paper_index} | from paper {paper_name}")
                    previous_index = paper_index
                print(
                    f'\tProcessed: {current_title[:50]}...{' '*(50-len(current_title[:50]))} (Queue size: {len(queue)})')

                # Respect API limits (Free tier is ~1 request per second)
                sleep(1.1)
                number_of_papers += 1

            except Exception as e:
                print(f"Connection error: {e}")
                sleep(5)

        # return results
        return number_of_papers

    def start_snowballing(
        self,
        save_path: Path,
        min_year: int = 2021,
        max_level: int = 2,
    ) -> list[dict]:
        previous_index = 0
        number_of_papers = len(self.paper_pool)
        results = []

        print(f"Total papers to process: {number_of_papers}")

        for index, paper in enumerate(self.paper_pool):
            print(
                f"Index: {index + 1}/{number_of_papers} ({index / number_of_papers * 100:.2f}%) | from paper {paper['title']}")
            paper_name = paper['title'].replace('/', '_').replace(':', '_')
            number_pf_ref_papers = self.fetch_citations_recursive(
                seed_ids=[paper],
                api_key=self.api_key,
                save_path=save_path,
                min_year=min_year,
                paper_index=index + 1,
                previous_index=previous_index,
                paper_name=paper_name,
                max_level=max_level
            )

            previous_index = index + 1
            print(
                f'\tTotal papers fetched from this seed: {number_pf_ref_papers}\n')
            results.append({
                'title': paper['title'],
                'doi': paper['doi'],
                'number_of_references': number_pf_ref_papers
            })

        return results
