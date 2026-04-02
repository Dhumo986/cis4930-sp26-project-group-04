"""
storage.py - Handles saving repo records to CSV and SQLite.
TODO: Implemented by Teammate 3 (Thomas or Imran).
"""


def save_to_csv(records: list, filepath: str):
    """
    Save records to a CSV file, appending if it already exists.

    Args:
        records:  List of dicts with repo data
        filepath: Path to the CSV file (e.g., data/processed/github_repos.csv)

    Notes:
        - Use pandas.DataFrame(records)
        - Use df.to_csv(filepath, mode='a', header=not os.path.exists(filepath), index=False)
        - Create parent directories if they don't exist
    """
    # TODO: Teammate implements this
    raise NotImplementedError("save_to_csv not yet implemented.")


def save_to_sqlite(records: list, filepath: str):
    """
    Save records to a SQLite database, appending new rows each run.

    Args:
        records:  List of dicts with repo data
        filepath: Path to the SQLite .db file (e.g., data/processed/github_repos.db)

    Notes:
        - Table name: repo_snapshots
        - Key columns: run_timestamp, repo_id, full_name, stargazers_count
        - Use df.to_sql("repo_snapshots", conn, if_exists="append", index=False)
    """
    # TODO: Teammate implements this
    raise NotImplementedError("save_to_sqlite not yet implemented.")
