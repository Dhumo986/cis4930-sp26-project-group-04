"""
pipeline.py - Main orchestrator for the GitHub Repository Activity Tracker
Fetches Python education repos from GitHub API and stores results locally.

Usage:
    python3 src/pipeline.py
    python3 src/pipeline.py --query "python machine learning" --max-pages 5 --per-page 20
"""

import argparse
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

# Import teammates' modules
try:
    from api_client import fetch_repos
except ImportError:
    logger.error("api_client.py not found. Make sure your teammate has implemented it.")
    raise

try:
    from storage import save_to_csv, save_to_sqlite
except ImportError:
    logger.error("storage.py not found. Make sure your teammate has implemented it.")
    raise


CSV_PATH    = "data/processed/github_repos.csv"
SQLITE_PATH = "data/processed/github_repos.db"


def parse_args():
    """Parse optional command-line arguments."""
    parser = argparse.ArgumentParser(
        description="GitHub Repository Activity Tracker Pipeline"
    )
    parser.add_argument(
        "--query",
        type=str,
        default="python education",
        help='Search query for GitHub repos (default: "python education")'
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=3,
        help="Maximum number of pages to fetch (default: 3)"
    )
    parser.add_argument(
        "--per-page",
        type=int,
        default=30,
        help="Number of results per page (default: 30, max: 100)"
    )
    return parser.parse_args()


def run_pipeline(query: str, max_pages: int, per_page: int):
    """Main pipeline: fetch → store."""
    logger.info("Starting pipeline run...")
    logger.info(f"Query: {query}")

    # Step 1: Fetch repo data (pagination handled in api_client)
    records = fetch_repos(query=query, max_pages=max_pages, per_page=per_page)

    if not records:
        logger.warning("No records fetched. Exiting pipeline.")
        return

    logger.info(f"Collected {len(records)} repositories.")

    # Step 2: Save to CSV
    save_to_csv(records, CSV_PATH)
    logger.info(f"Appended {len(records)} rows to {CSV_PATH}")

    # Step 3: Save to SQLite
    save_to_sqlite(records, SQLITE_PATH)

    logger.info("Pipeline completed successfully.")


if __name__ == "__main__":
    args = parse_args()
    run_pipeline(
        query=args.query,
        max_pages=args.max_pages,
        per_page=args.per_page
    )
