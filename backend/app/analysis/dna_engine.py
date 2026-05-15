def developer_dna_analysis(repositories):

    repository_count = len(repositories)

    if repository_count >= 10:

        developer_type = (
            "Rapid Builder"
        )

    else:

        developer_type = (
            "Focused Developer"
        )

    return {
        "developer_type": developer_type,

        "traits": [
            "Fast project execution",
            "High experimentation",
            "Backend focused"
        ]
    }
