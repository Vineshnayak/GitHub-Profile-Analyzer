def generate_markdown_resume(
    resume_data
):

    markdown = f"""
# {resume_data['name']}

## Professional Summary

{resume_data['summary']}

---

## Technical Skills

"""

    for skill in resume_data["skills"]:

        markdown += f"- {skill}\n"

    markdown += "\n---\n"

    markdown += "## Projects\n\n"

    for project in resume_data["projects"]:

        markdown += (
            f"### {project['name']}\n"
        )

        markdown += (
            f"{project['description']}\n\n"
        )

        markdown += (
            f"- Language: "
            f"{project['language']}\n"
        )

        markdown += (
            f"- Stars: "
            f"{project['stars']}\n\n"
        )

    return markdown
