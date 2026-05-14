from fastapi import APIRouter, HTTPException

from app.services.github_service import (
    get_user_profile,
    get_user_repositories
)

from app.analysis.profile_analyzer import analyze_profile

router = APIRouter()


@router.get("/analyze/{username}")
def analyze_github_profile(username: str):

    # Remove spaces
    username = username.strip()

    # Validate username
    if len(username) < 1:
        raise HTTPException(
            status_code=400,
            detail="Username cannot be empty"
        )

    # Fetch GitHub profile
    profile = get_user_profile(username)

    # User not found
    if not profile:
        raise HTTPException(
            status_code=404,
            detail="GitHub user not found"
        )

    # Fetch repositories
    repositories = get_user_repositories(username)

    # Analyze profile
    analysis_result = analyze_profile(
        profile,
        repositories
    )

    return analysis_result
