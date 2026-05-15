import requests

from app.config.settings import (
    settings
)

from app.utils.cache import (
    get_cache,
    set_cache
)

from app.utils.logger import (
    logger
)


class GitHubService:

    @staticmethod
    def get_profile(username: str):

        cache_key = (
            f"profile_{username}"
        )

        cached_data = (
            get_cache(cache_key)
        )

        if cached_data:

            logger.info(
                f"Cache hit: {username}"
            )

            return cached_data

        url = (
            f"{settings.GITHUB_API_URL}"
            f"/users/{username}"
        )

        logger.info(
            f"Fetching profile: "
            f"{username}"
        )

        response = requests.get(url)

        if response.status_code != 200:

            logger.error(
                f"GitHub API error: "
                f"{response.status_code}"
            )

            return None

        data = response.json()

        set_cache(
            cache_key,
            data
        )

        return data

    @staticmethod
    def get_repositories(
        username: str
    ):

        cache_key = (
            f"repos_{username}"
        )

        cached_data = (
            get_cache(cache_key)
        )

        if cached_data:

            logger.info(
                f"Repo cache hit: "
                f"{username}"
            )

            return cached_data

        url = (
            f"{settings.GITHUB_API_URL}"
            f"/users/{username}/repos"
        )

        logger.info(
            f"Fetching repositories: "
            f"{username}"
        )

        response = requests.get(url)

        if response.status_code != 200:

            logger.error(
                "Repository fetch failed"
            )

            return []

        data = response.json()
        filtered_repositories = [
            repo
            for repo in data
            if not repo.get("fork")
        ]
        set_cache(
            cache_key,
            filtered_repositories
        )
        return filtered_repositories
