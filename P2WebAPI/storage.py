"""Storage helpers for appending weather records to CSV and SQLite."""

from __future__ import annotations

import logging
import sqlite3
from pathlib import Path
from typing import Mapping, Sequence

import pandas as pd

logger = logging.getLogger(__name__)


def _to_dataframe(records: Sequence[Mapping] | pd.DataFrame) -> pd.DataFrame:
    """Convert API records to a DataFrame with stable column order."""
    if isinstance(records, pd.DataFrame):
        df = records.copy()
    else:
        df = pd.DataFrame.from_records(records)

    if df.empty:
        return df

    # Keep columns stable for repeatable CSV/SQLite outputs.
    return df.reindex(sorted(df.columns), axis=1)


def save_to_csv(records: Sequence[Mapping] | pd.DataFrame, filepath: str) -> int:
    """Append records to CSV and return number of rows written."""
    df = _to_dataframe(records)
    if df.empty:
        logger.info("No records to write to CSV.")
        return 0

    target = Path(filepath)
    target.parent.mkdir(parents=True, exist_ok=True)
    file_exists = target.exists()

    df.to_csv(target, mode="a", index=False, header=not file_exists)
    logger.info("Appended %s rows to CSV: %s", len(df), target)
    return int(len(df))


def save_to_sqlite(
    records: Sequence[Mapping] | pd.DataFrame,
    filepath: str,
    table_name: str = "weather_records",
) -> int:
    """Append records to SQLite table and return number of rows written."""
    df = _to_dataframe(records)
    if df.empty:
        logger.info("No records to write to SQLite.")
        return 0

    target = Path(filepath)
    target.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(target) as conn:
        df.to_sql(table_name, conn, if_exists="append", index=False)

    logger.info("Appended %s rows to SQLite table '%s': %s", len(df), table_name, target)
    return int(len(df))
