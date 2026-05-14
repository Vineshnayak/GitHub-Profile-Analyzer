import logging
import requests

from app.config import GITHUB_TOKEN

# Logger setup
logger = logging.getLogger(__name__)

# Base GitHub API URL
BASE_URL = "https://api.github.com"

# Request headers
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}"
}


def get_user_profile(username: str):
    """
    Fetch GitHub user profile
    """

    try:

        url = f"{BASE_URL}/users/{username}"

        logger.info(f"Fetching profile for {username}")

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=10
        )

        # User not found
        if response.status_code == 404:
            logger.warning(f"User not found: {username}")
            return None

        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        logger.error("GitHub API timeout")
        return None

    except requests.exceptions.RequestException as error:
        logger.error(f"GitHub API error: {error}")
        return None


def get_user_repositories(username: str):
    """
    Fetch GitHub repositories
    """

    try:

        url = f"{BASE_URL}/users/{username}/repos"

        logger.info(f"Fetching repositories for {username}")

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=10
        )

        if response.status_code != 200:
            logger.warning(
                f"Failed fetching repos for {username}"
            )
            return []

        return response.json()

    except requests.exceptions.Timeout:
        logger.error("Repository request timeout")
        return []

    except requests.exceptions.RequestException as error:
        logger.error(f"Repository fetch error: {error}")
        return []
   