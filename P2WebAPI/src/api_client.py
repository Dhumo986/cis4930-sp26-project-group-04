"""
api_client.py - Handles HTTP requests and pagination for the GitHub REST API.
TODO: Implemented by Teammate 2 (Thomas or Imran).
"""

import requests

BASE_URL = "https://api.github.com/search/repositories"


def fetch_repos(query: str, max_pages: int = 3, per_page: int = 30) -> list:
    """
    Fetch repository records from GitHub API across multiple pages.

    Args:
        query:     Search query string (e.g., "python education")
        max_pages: Maximum number of pages to fetch
        per_page:  Number of results per page (max 100)

    Returns:
        List of dicts, each representing one repository record with fields:
        run_timestamp, repo_id, full_name, html_url, description,
        stargazers_count, forks_count, open_issues_count, language,
        created_at, updated_at
    """
    # TODO: Teammate implements this using:
    # - requests.get(BASE_URL, params=params, timeout=10)
    # - response.raise_for_status() inside try/except
    # - pagination loop: for page in range(1, max_pages + 1)
    # - item.get("field", default) for safe access
    # - catch requests.exceptions.Timeout and RequestException
    raise NotImplementedError("api_client.py not yet implemented.")
