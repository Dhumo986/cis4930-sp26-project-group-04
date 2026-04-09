"""
pipeline.py - Main orchestrator for the GitHub Repository Activity Tracker
Fetches Python education repos from GitHub API and stores results locally.
"""

import logging
import os
from datetime import datetime

# Configure logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/pipeline.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

try:
    from api_client import fetch_repos
except ImportError:
    logger.error("api_client.py not found.")
    raise

try:
    from storage import save_to_csv, save_to_sqlite
except ImportError:
    logger.error("storage.py not found.")
    raise


QUERY     = "python education"
MAX_PAGES = 3
PER_PAGE  = 30

CSV_PATH    = "data/processed/github_repos.csv"
SQLITE_PATH = "data/processed/github_repos.db"


def run_pipeline():
    """Main pipeline: fetch → store."""
    logger.info("Starting pipeline run...")
    logger.info(f"Query: {QUERY}")

    # Step 1: Fetch repo data (pagination handled in api_client)
    records = fetch_repos(query=QUERY, max_pages=MAX_PAGES, per_page=PER_PAGE)

    if not records:
        logger.warning("No records fetched. Exiting pipeline.")
        return

    logger.info(f"Collected {len(records)} repositories.")

    # Step 2: Save to CSV
    save_to_csv(records, CSV_PATH)
    logger.info(f"Appended {len(records)} rows to {CSV_PATH}")

    # Step 3: Save to SQLite (optional)
    save_to_sqlite(records, SQLITE_PATH)

    logger.info("Pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()
