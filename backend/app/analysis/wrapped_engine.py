from collections import Counter

from app.services.commit_service import (
    CommitService
)

from app.analysis.contribution_engine import (
    analyze_contributions
)


def generate_wrapped_data(
    profile,
    repositories
):

    total_repositories = len(
        repositories
    )

    total_stars = sum(

        repo["stargazers_count"]

        for repo in repositories
    )

    languages = [

        repo["language"]

        for repo in repositories

        if repo["language"]
    ]

    language_counter = Counter(
        languages
    )

    top_languages = (
        language_counter.most_common(5)
    )

    top_repositories = sorted(

        repositories,

        key=lambda repo:
            repo["stargazers_count"],

        reverse=True

    )[:5]

    productivity_score = min(

        total_repositories * 5 +
        total_stars * 2,

        100
    )

    commit_data = []

    for repo in repositories[:5]:

        commits = (
            CommitService
            .get_repository_commits(

                profile["login"],

                repo["name"]
            )
        )

        commit_data.append(
            commits
        )

    contribution_data = (
        analyze_contributions(
            repositories,
            commit_data
        )
    )

    return {

        "username":
            profile["login"],

        "total_repositories":
            total_repositories,

        "total_stars":
            total_stars,

        "top_languages":
            top_languages,

        "productivity_score":
            productivity_score,

        "top_repositories": [

            {
                "name":
                    repo["name"],

                "stars":
                    repo["stargazers_count"],

                "language":
                    repo["language"]
            }

            for repo in top_repositories
                ],

        "contribution_analytics":
            contribution_data
    }
