from fastapi import (
    APIRouter,
    HTTPException
)

from app.services.github_service import (
    GitHubService
)

from app.utils.helpers import (
    calculate_language_stats
)

from app.analysis.resume_engine import (
    generate_resume_data
)

from app.utils.resume_generator import (
    generate_markdown_resume
)

router = APIRouter()


@router.get("/{username}")
def generate_resume(username: str):

    profile = (
        GitHubService.get_profile(username)
    )

    if not profile:

        raise HTTPException(
            status_code=404,
            detail="GitHub user not found"
        )

    repositories = (
        GitHubService.get_repositories(
            username
        )
    )

    language_stats = (
        calculate_language_stats(
            repositories
        )
    )

    resume_data = (
        generate_resume_data(
            profile,
            repositories,
            language_stats
        )
    )

    markdown_resume = (
        generate_markdown_resume(
            resume_data
        )
    )

    return {

        "resume_data":
            resume_data,

        "markdown_resume":
            markdown_resume
    }
