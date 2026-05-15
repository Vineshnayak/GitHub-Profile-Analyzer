from pydantic import BaseModel

from typing import (
    List,
    Dict,
    Any
)


class ProfileModel(BaseModel):

    username: str

    name: str | None

    bio: str | None

    followers: int

    following: int

    public_repos: int

    profile_url: str

    avatar_url: str


class RepositoryModel(BaseModel):

    name: str

    language: str | None

    stars: int

    forks: int


class ProfileResponseModel(
    BaseModel
):

    profile: ProfileModel

    developer_score: int

    repositories: List[
        RepositoryModel
    ]

    language_stats: Dict

    recruiter_analysis: Dict[
        str,
        Any
    ]

    developer_dna: Dict[
        str,
        Any
    ]

    startup_readiness: Dict[
        str,
        Any
    ]