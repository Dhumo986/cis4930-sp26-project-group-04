# Contribution Reports — CIS 4930 Group 04

> Automated Data Pipeline from Web APIs<br>
> GitHub API<br>
> Spring 2026

---

## Contribution Report — Thomas Schmidt
### FSU ID: TNS23


### Contributions

- **`src/api_client.py`** — Wrote the GitHub REST API client from scratch, including:
  - HTTP requests with `requests.get` using query parameters and a 10s timeout
  - Page-based pagination loop (`page=1..max_pages`) with early termination on empty results
  - Error handling `try/except` catching both `Timeout` and `RequestException`
  - JSON parsing and extraction of 11 fields per repo
  - Dual logging to both `logs/api_client.log` and console

- **`src/storage.py`** — Rewrote and simplified the storage module:
  - Refactored down to clean `save_to_csv` and `save_to_sqlite` helpers
  - Fixed SQLite connection to use a context manager (`with sqlite3.connect(...)`) to prevent resource leaks

- **Pipeline testing and data generation** — Ran the pipeline multiple times to produce the output dataset (`data/processed/github_repos.csv`, 210 records across 3 runs)

### Merge and Integration

- Resolved merge conflict when merging `pipeline-orchestration` into `main`
- Fixed README inconsistencies

## Git Contributions

| Branch | Purpose |
|--------|---------|
| `pipeline-orchestration` | Main branch I worked on with Dhruv |
| `main` | merged pipeline-orchestration -> main and fixed conflicts |