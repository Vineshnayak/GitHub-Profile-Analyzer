from fastapi import (
    APIRouter,
    HTTPException
)

from app.services.github_service import (
    GitHubService
)

from app.analysis.wrapped_engine import (
    generate_wrapped_data
)

router = APIRouter()


@router.get("/{username}")
def github_wrapped(username: str):

    profile = (
        GitHubService.get_profile(
            username
        )
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

    wrapped_data = (
        generate_wrapped_data(
            profile,
            repositories
        )
    )

    return wrapped_data
