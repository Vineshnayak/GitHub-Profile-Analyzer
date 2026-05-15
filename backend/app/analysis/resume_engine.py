def generate_resume_data(
    profile,
    repositories,
    language_stats
):

    skills = list(
        language_stats.keys()
    )

    projects = []

    for repo in repositories[:5]:

        projects.append({

            "name":
                repo["name"],

            "description":
                repo.get(
                    "description",
                    "No description provided"
                ),

            "language":
                repo["language"],

            "stars":
                repo["stargazers_count"]
        })

    summary = (
        f"{profile['login']} is a "
        f"software developer with "
        f"experience in "
        f"{', '.join(skills)}."
    )

    return {

        "name":
            profile.get("name"),

        "username":
            profile["login"],

        "summary":
            summary,

        "skills":
            skills,

        "projects":
            projects
    }
