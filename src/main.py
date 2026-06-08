import json
import src.config as config

from pathlib import Path

from src.snowballing import Snowballing



def main():
    cwd = Path.cwd()
    if 'src' in cwd.parts:
        root_path = cwd.parent
    else:
        root_path = cwd
    dataset_path = root_path.joinpath('data')

    sample_papers_path = dataset_path.joinpath('filtered_papers/classified_sample_papers.jsonl')
    snowballing_path = Path(r'/mnt/ext-hdd1/P/snowballing_papers')

    semantic_scholar_api_key = config.SEMANTIC_SCHOLAR_API_KEY
    print(sample_papers_path)

    with open(sample_papers_path, 'r') as f:
        data = [json.loads(line) for line in f]

    paper_pool = [
        {'title': paper['title'], 'doi': paper['link'].replace('https://doi.org/', '')} for paper in data
    ]

    # print(json.dumps(paper_pool, indent=4))

    snowballing = Snowballing(
        api_key=semantic_scholar_api_key,
        paper_pool=paper_pool
    )

    res = snowballing.start_snowballing(
        save_path=snowballing_path,
        min_year=2021
    )

    print(json.dumps(res, indent=4))

    return


if __name__ == '__main__':
    main()