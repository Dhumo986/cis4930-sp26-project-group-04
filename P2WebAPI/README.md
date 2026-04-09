# Automated Data Pipeline from Web APIs

**Course:** CIS 4930 — Introduction to Python (Spring 2026)  
**Group:** 04

## Group Members

| Name | FSU ID |
|---|---|
| Thomas Schmidt | tns23@fsu.edu |
| Imran Ahmed | ia24c@fsu.edu |
| Dhruv Upadhyay | dtu24@fsu.edu |

---

## Project Title

**GitHub Repository Activity Tracker**

## Project Description

This project builds an automated Python data pipeline that collects repository metadata from the GitHub REST API for education-related Python projects. On each run, the pipeline fetches multiple pages of results, handles request errors safely, and appends structured records to a local CSV (and optionally SQLite) data store for longitudinal analysis.

Real-world context: this can be used to monitor trends in open-source learning resources, repository popularity, and language usage over time.

---

## API Documentation

- GitHub REST API docs: https://docs.github.com/en/rest
- Search repositories endpoint: https://docs.github.com/en/rest/search/search#search-repositories

---

## Why This API

The GitHub API is relevant because it provides real, high-volume public data that changes over time. It supports meaningful pagination and query parameters, making it ideal for demonstrating robust HTTP requests, JSON parsing, and incremental data collection.

### API Constraints

- **Rate limits:** unauthenticated requests are limited (GitHub rate limiting applies).
- **Pagination:** page-based (`page`, `per_page`) with finite result windows.
- **Auth:** optional token can increase limits; this project works without auth for classroom-scale runs.

---

## Data Pipeline Goals

1. Fetch repository data for a configurable query (default: `python education`).
2. Collect multiple pages per run (e.g., 3–5 pages, `per_page=30`).
3. Extract and store at least 5 meaningful fields per repository.
4. Handle failures (timeouts/request errors) without crashing silently.
5. Append new rows to a persistent dataset on repeated runs.

---

## Planned Repository Structure

```text
P2WebAPI/
├── README.md
├── src/
│   ├── pipeline.py          # Main orchestration script
│   ├── api_client.py        # HTTP requests + pagination
│   └── storage.py           # CSV/SQLite write helpers
├── data/
│   └── processed/
│       └── github_repos.csv
└── logs/
	└── pipeline.log
```

---

## Minimum Technical Features

The implementation demonstrates:

- `requests.get(..., params=..., timeout=...)`
- JSON parsing via `response.json()`
- Safe field access with `.get()` defaults
- Pagination loop over multiple pages
- `try/except` with `raise_for_status()` and `RequestException`
- Conversion to `pandas.DataFrame`
- Persistent local storage with CSV and SQLite append

### Example Fields Collected

- `run_timestamp`
- `repo_id`
- `full_name`
- `html_url`
- `description`
- `stargazers_count`
- `forks_count`
- `open_issues_count`
- `language`
- `created_at`
- `updated_at`

---

## Data Output

Primary output:

- `data/processed/github_repos.csv` (appended across runs)
- SQLite database `data/processed/github_repos.db`
- Table name: `repo_snapshots`
- Key columns: `run_timestamp`, `repo_id`, `full_name`, `stargazers_count`

---

## How to Run

From the `P2WebAPI` directory:

First, create a virtual enviroment and source it. Then, install the requirements (pandas, requests).

```bash
pip install -r requirements.txt
```

Then, run the pipeline:

```bash
python src/pipeline.py
```

### Example Console Output

```text
[INFO] Starting pipeline run...
[INFO] Query: python education
[INFO] Fetching page 1...
[INFO] Fetching page 2...
[INFO] Fetching page 3...
[INFO] Collected 90 repositories.
[INFO] Appended 90 rows to data/processed/github_repos.csv
[INFO] Pipeline completed successfully.
```

---

## Error Handling Strategy

- Timeout handling with clear fallback message
- Request-level exception handling (`requests.exceptions.RequestException`)
- Status validation with `response.raise_for_status()`
- Graceful skip/continue behavior instead of silent failure
- Optional log persistence to `logs/pipeline.log`

---

## Automation Hook (Optional)

Example cron schedule (every day at 8:00 AM):

```cron
0 8 * * * /usr/bin/python3 /path/to/P2WebAPI/src/pipeline.py
```

---

## Team Workflow
- PR-based merges into main
- Commit history reflects contributions from all members

Role split (rotating):

- API client lead: HTTP + pagination
- Data/storage lead: DataFrame + CSV/SQLite
- Robustness lead: logging + retries + exceptions
- Documentation lead: README + run notes

---

## Stretch Goals (Bonus)

- Add CLI arguments (`--query`, `--max-pages`, `--per-page`)
- Add retry/backoff for temporary API failures
- Add a mini EDA notebook with 1–2 plots from generated CSV
