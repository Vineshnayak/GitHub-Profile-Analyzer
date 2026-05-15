def calculate_developer_score(
    profile,
    repositories
):

    score = 0

    repository_count = len(repositories)

    total_stars = sum(
        repo["stargazers_count"]
        for repo in repositories
    )

    followers = profile["followers"]

    score += repository_count * 5
    score += total_stars * 2
    score += followers * 1

    return min(score, 100)
