"""
storage.py - Handles saving repo records to CSV and SQLite.
"""

import os
import sqlite3

import pandas as pd


def save_to_csv(records: list, filepath: str):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df = pd.DataFrame(records)
    df.to_csv(filepath, mode="a", header=not os.path.exists(filepath), index=False)


def save_to_sqlite(records: list, filepath: str):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    conn = sqlite3.connect(filepath)
    df = pd.DataFrame(records)
    df.to_sql("repo_snapshots", conn, if_exists="append", index=False)
    conn.close()
