def recruiter_analysis(repositories):

    languages = []

    for repo in repositories:

        language = repo.get("language")

        if language:
            languages.append(language)

    roles = []

    if "Python" in languages:
        roles.append(
            "Backend Developer"
        )

    if "JavaScript" in languages:
        roles.append(
            "Frontend Developer"
        )

    if "Docker" in str(repositories):
        roles.append(
            "DevOps Engineer"
        )

    strengths = [
        "API Development",
        "Automation"
    ]

    weaknesses = [
        "Testing",
        "System Design"
    ]

    return {
        "recommended_roles": roles,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "hiring_confidence": 84
    }
