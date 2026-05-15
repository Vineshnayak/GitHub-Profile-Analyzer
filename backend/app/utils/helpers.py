def calculate_language_stats(repositories):

    language_count = {}

    for repo in repositories:

        language = repo.get("language")

        if language:

            language_count[language] = (
                language_count.get(language, 0) + 1
            )

    return language_count
