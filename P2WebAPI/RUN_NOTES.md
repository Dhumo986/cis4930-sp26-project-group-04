# RUN_NOTES.md

## How to Run the Pipeline

### Prerequisites

Install dependencies from the `P2WebAPI` directory:

```bash
pip install -r requirements.txt
```

### Run the pipeline

```bash
# From the P2WebAPI directory
python3 src/pipeline.py
```

### Example Console Output

```
2026-04-09 22:20:37,519 [INFO] Starting pipeline run...
2026-04-09 22:20:37,519 [INFO] Query: python education
2026-04-09 22:20:38,724 [INFO] fetched page 1 — 30 items
2026-04-09 22:20:39,887 [INFO] fetched page 2 — 30 items
2026-04-09 22:20:41,051 [INFO] fetched page 3 — 30 items
2026-04-09 22:20:41,053 [INFO] Collected 90 repositories.
2026-04-09 22:20:41,067 [INFO] Appended 90 rows to data/processed/github_repos.csv
2026-04-09 22:20:41,072 [INFO] Pipeline completed successfully.
```

### Output Files

- `data/processed/github_repos.csv` — appends new rows on every run
- `data/processed/github_repos.db` — SQLite database with `repo_snapshots` table
- `logs/pipeline.log` — full run log history

### Simulating Scheduled Runs

Run the script multiple times to simulate daily data accumulation:

```bash
python3 src/pipeline.py  # Run 1 — appends 90 rows
python3 src/pipeline.py  # Run 2 — appends another 90 rows
python3 src/pipeline.py  # Run 3 — appends another 90 rows
```

Each run adds new rows with a fresh `run_timestamp` so you can track changes over time.

### Optional: Cron Scheduling (Linux/Mac)

To run automatically every day at 8:00 AM, add to crontab (`crontab -e`):

```
0 8 * * * /usr/bin/python3 /path/to/P2WebAPI/src/pipeline.py
```

### Optional: Windows Task Scheduler

Create a `run_pipeline.bat` file:

```bat
@echo off
python src\pipeline.py
```

Then schedule it via Windows Task Scheduler to run daily.
