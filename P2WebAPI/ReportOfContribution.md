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

---

## Contribution Report — Dhruv Upadhyay
### FSU ID: DTU24

### Contributions

- **`src/pipeline.py`** — Wrote the main orchestration script, including:
  - Logging setup with dual handlers (console + `logs/pipeline.log`)
  - Graceful `ImportError` handling for missing teammate modules
  - Full pipeline flow: fetch → save to CSV → save to SQLite
  - **CLI argument support** (bonus feature) using `argparse`:
    - `--query` to set the GitHub search query
    - `--max-pages` to control pagination depth
    - `--per-page` to set results per page
  - Verified end-to-end pipeline run producing 90 records across 3 pages

- **`RUN_NOTES.md`** — Wrote full run documentation including:
  - Install instructions
  - Example console output matching actual pipeline output
  - Instructions for simulating scheduled runs
  - Cron and Windows Task Scheduler examples

- **`README.md`** — Updated and corrected the project README:
  - Fixed group member table (correct FSU IDs, removed departed member)
  - Updated repository structure to reflect actual built structure
  - Fixed example console output to match real pipeline output
  - Added CLI arguments table for bonus feature
  - Corrected "Planned" → actual structure

- **`.gitignore`** — Created project-level gitignore excluding:
  - Generated CSV/SQLite data files
  - Log files
  - Python `__pycache__` and `.pyc` files
  - OS and editor artifacts

- **Repo setup and GitHub workflow** — Set up the `P2WebAPI/` directory structure, created feature branch `pipeline-orchestration`, and managed PR to main.

### Git Contributions

| Branch | Purpose |
|--------|---------|
| `pipeline-orchestration` | All pipeline orchestration work, README, RUN_NOTES, .gitignore |
| `main` | Final merge after conflict resolution |

---

## Contribution Report — Imran Ahmed
### FSU ID: IA24C

### Contributions

- **`src/storage.py`** — Implemented the data storage module, including:
  - `save_to_csv()` function using `pandas.DataFrame` with append mode so repeated runs accumulate data
  - `save_to_sqlite()` function using `sqlite3` context manager and `df.to_sql()` with `if_exists="append"`
  - Automatic directory creation with `os.makedirs(..., exist_ok=True)`
  - Table name: `repo_snapshots` with key columns: `run_timestamp`, `repo_id`, `full_name`, `stargazers_count`

- **`requirements.txt`** — Generated and documented all project dependencies

- **Integration testing** — Verified that `save_to_csv` and `save_to_sqlite` correctly interface with `pipeline.py` and `api_client.py` outputs

### Git Contributions

| Branch | Purpose |
|--------|---------|
| `storage-and-docs` | Storage module, requirements.txt, data directory setup |
| `main` | Merged storage branch into main |
