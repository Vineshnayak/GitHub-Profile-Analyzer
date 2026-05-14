from collections import Counter


def analyze_profile(profile, repositories):
    """
    Main analysis function
    """

    # Store language usage
    languages = []

    # Track repository statistics
    total_stars = 0
    total_forks = 0

    # Repository activity score
    active_repositories = 0

    # Store repository summaries
    repository_summaries = []

    # Process repositories
    for repo in repositories:

        # Repository language
        language = repo.get("language")

        if language:
            languages.append(language)

        # Stars
        total_stars += repo.get("stargazers_count", 0)

        # Forks
        total_forks += repo.get("forks_count", 0)

        # Repository summaries
        repository_summaries.append({
            "name": repo.get("name"),
            "language": repo.get("language"),
            "stars": repo.get("stargazers_count"),
            "forks": repo.get("forks_count")
        })

        # Activity detection
        if not repo.get("fork"):
            active_repositories += 1

    # Count languages
    language_counter = Counter(languages)

    # Top languages
    top_languages = dict(language_counter.most_common(5))

    # Tech stack list
    tech_stack = list(language_counter.keys())

    # Developer score calculation
    developer_score = calculate_developer_score(
        followers=profile.get("followers", 0),
        repositories_count=profile.get("public_repos", 0),
        stars=total_stars,
        active_repositories=active_repositories
    )

    # Final analysis result
    analysis_result = {
        "username": profile.get("login"),
        "name": profile.get("name"),
        "bio": profile.get("bio"),

        "followers": profile.get("followers"),
        "following": profile.get("following"),

        "public_repositories": profile.get("public_repos"),

        "total_stars": total_stars,
        "total_forks": total_forks,

        "active_repositories": active_repositories,

        "top_languages": top_languages,

        "tech_stack": tech_stack,

        "repositories": repository_summaries,

        "repository_quality_score": min(total_stars // 10, 100),

        "developer_score": developer_score
    }

    return analysis_result


def calculate_developer_score(
    followers,
    repositories_count,
    stars,
    active_repositories
):
    """
    Simple developer score system
    """

    score = 0

    # Followers score
    score += min(followers * 0.2, 20)

    # Repository score
    score += min(repositories_count * 1.5, 30)

    # Stars score
    score += min(stars * 0.05, 30)

    # Active repositories score
    score += min(active_repositories * 2, 20)

    return round(score)