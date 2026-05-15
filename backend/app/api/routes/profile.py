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

from app.analysis.scoring_engine import (
    calculate_developer_score
)

from app.analysis.recruiter_engine import (
    recruiter_analysis
)

from app.analysis.dna_engine import (
    developer_dna_analysis
)

from app.analysis.startup_engine import (
    startup_readiness_analysis
)

from app.models.response_models import (
    ProfileResponseModel
)

router = APIRouter()


@router.get(
    "/{username}",
    response_model=ProfileResponseModel
)
def analyze_profile(username: str):

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

    developer_score = (
        calculate_developer_score(
            profile,
            repositories
        )
    )

    recruiter_data = (
        recruiter_analysis(
            repositories
        )
    )

    dna_data = (
        developer_dna_analysis(
            repositories
        )
    )

    startup_data = (
        startup_readiness_analysis(
            repositories
        )
    )

    repository_data = []

    for repo in repositories:

        repository_data.append({

            "name":
                repo["name"],

            "language":
                repo["language"],

            "stars":
                repo["stargazers_count"],

            "forks":
                repo["forks_count"]
        })

    profile_response = {

        "username":
            profile["login"],

        "name":
            profile.get("name"),

        "bio":
            profile.get("bio"),

        "followers":
            profile["followers"],

        "following":
            profile["following"],

        "public_repos":
            profile["public_repos"],

        "profile_url":
            profile["html_url"],

        "avatar_url":
            profile["avatar_url"]
    }

    return {

        "profile":
            profile_response,

        "developer_score":
            developer_score,

        "repositories":
            repository_data,

        "language_stats":
            language_stats,

        "recruiter_analysis":
            recruiter_data,

        "developer_dna":
            dna_data,

        "startup_readiness":
            startup_data
    }
