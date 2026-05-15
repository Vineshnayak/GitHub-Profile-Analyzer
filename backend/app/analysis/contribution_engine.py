from collections import Counter
from datetime import datetime


def analyze_contributions(
    repositories,
    commit_data
):

    total_commits = 0

    commit_hours = []

    commit_dates = []

    for repository_commits in commit_data:

        total_commits += len(
            repository_commits
        )

        for commit in repository_commits:

            try:

                commit_info = (
                    commit["commit"]
                )

                commit_date = (
                    commit_info["author"]
                    ["date"]
                )

                parsed_date = (
                    datetime.fromisoformat(
                        commit_date.replace(
                            "Z",
                            "+00:00"
                        )
                    )
                )

                commit_hours.append(
                    parsed_date.hour
                )

                commit_dates.append(
                    parsed_date.date()
                )

            except Exception:

                continue

    productive_hour = None

    if commit_hours:

        productive_hour = (
            Counter(
                commit_hours
            ).most_common(1)[0][0]
        )

    streak_estimate = len(
        set(commit_dates)
    )

    return {

        "total_commits":
            total_commits,

        "most_productive_hour":
            productive_hour,

        "estimated_active_days":
            streak_estimate
    }
