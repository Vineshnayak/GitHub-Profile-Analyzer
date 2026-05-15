import requests

from app.config.settings import (
    settings
)

from app.utils.logger import (
    logger
)


class CommitService:

    @staticmethod
    def get_repository_commits(
        username: str,
        repository: str
    ):

        url = (

            f"{settings.GITHUB_API_URL}"
            f"/repos/{username}/"
            f"{repository}/commits"
        )

        logger.info(
            f"Fetching commits for "
            f"{repository}"
        )

        response = requests.get(url)

        if response.status_code != 200:

            logger.error(
                "Commit fetch failed"
            )

            return []

        return response.json()
