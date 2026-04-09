"""
api_client.py - Handles HTTP requests and pagination for the GitHub REST API.
"""

import logging
import os
from datetime import datetime, timezone

import requests

os.makedirs("logs", exist_ok=True)
logger = logging.getLogger('API')
logger.setLevel(logging.INFO)
_fh = logging.FileHandler("logs/api_client.log")
_sh = logging.StreamHandler()
_fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
_fh.setFormatter(_fmt)
_sh.setFormatter(_fmt)
logger.addHandler(_fh)
logger.addHandler(_sh)
logger.propagate = False

BASE_URL = "https://api.github.com/search/repositories"


def fetch_repos(query: str, max_pages: int = 3, per_page: int = 30) -> list:
    records = []
    timestamp = datetime.now(timezone.utc).isoformat()

    for page in range(1, max_pages + 1):
        params = {"q": query, "per_page": per_page, "page": page}

        try:
            response = requests.get(BASE_URL, params=params, timeout=10)
            response.raise_for_status()
        except requests.exceptions.Timeout:
            logger.warning("request timed out on page %d, skipping", page)
            continue
        except requests.exceptions.RequestException as e:
            logger.error("request failed on page %d: %s", page, e)
            break

        data = response.json()
        items = data.get("items", [])

        if not items:
            break

        for item in items:
            records.append({
                "run_timestamp": timestamp,
                "repo_id": item.get("id"),
                "full_name": item.get("full_name", ""),
                "html_url": item.get("html_url", ""),
                "description": item.get("description", ""),
                "stargazers_count": item.get("stargazers_count", 0),
                "forks_count": item.get("forks_count", 0),
                "open_issues_count": item.get("open_issues_count", 0),
                "language": item.get("language", "Unknown"),
                "created_at": item.get("created_at", ""),
                "updated_at": item.get("updated_at", ""),
            })

        logger.info("fetched page %d — %d items", page, len(items))

    return records
