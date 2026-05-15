import streamlit as st


def render_wrapped_section(
    wrapped_data
):

    st.subheader(
        "GitHub Wrapped"
    )

    col1, col2, col3 = (
        st.columns(3)
    )

    with col1:

        st.metric(

            "Productivity Score",

            wrapped_data[
                "productivity_score"
            ]
        )

    with col2:

        st.metric(

            "Total Stars",

            wrapped_data[
                "total_stars"
            ]
        )

    with col3:

        st.metric(

            "Repositories",

            wrapped_data[
                "total_repositories"
            ]
        )

    st.markdown("---")

    contribution = (
        wrapped_data[
            "contribution_analytics"
        ]
    )

    st.write(
        "Contribution Analytics"
    )

    st.info(

        f"Total Commits: "
        f"{contribution['total_commits']}"
    )

    st.info(

        f"Most Productive Hour: "
        f"{contribution['most_productive_hour']}:00"
    )

    st.info(

        f"Estimated Active Days: "
        f"{contribution['estimated_active_days']}"
    )

    st.markdown("---")

    st.write("Top Languages")

    for language in wrapped_data[
        "top_languages"
    ]:

        st.write(
            f"• {language[0]} "
            f"({language[1]})"
        )