import streamlit as st
import pandas as pd

from components.sidebar import (
    render_sidebar
)

from components.cards import (
    render_profile_cards
)

from components.charts import (
    render_language_chart
)

from components.wrapped import (
    render_wrapped_section
)

from components.dna import (
    render_dna_section
)

from components.startup import (
    render_startup_section
)

from utils.api_client import (
    get_profile_data,
    get_wrapped_data,
    get_resume_data
)

st.set_page_config(

    page_title=
        "GitHub Profile Analyzer",

    layout="wide"
)

st.title(
    "GitHub Profile Analyzer"
)

st.caption(
    "AI-powered developer analytics "
    "platform"
)

username, analyze_button = (
    render_sidebar()
)

if analyze_button and username:

    with st.spinner(
        "Analyzing GitHub profile..."
    ):

        profile_data = (
            get_profile_data(username)
        )

        wrapped_data = (
            get_wrapped_data(username)
        )

        resume_data = (
            get_resume_data(username)
        )

    if not profile_data:

        st.error(
            "GitHub user not found"
        )

    else:

        profile = (
            profile_data["profile"]
        )

        col1, col2 = st.columns(
            [1, 4]
        )

        with col1:

            st.image(
                profile["avatar_url"],
                width=140
            )

        with col2:

            st.header(
                profile["name"]
            )

            st.write(
                profile["bio"]
            )

            st.markdown(

                f"""
                🔗 [GitHub Profile]
                ({profile['profile_url']})
                """
            )

        st.markdown("---")

        render_profile_cards(
            profile
        )

        st.markdown("---")

        render_language_chart(

            profile_data[
                "language_stats"
            ]
        )

        st.markdown("---")

        st.subheader(
            "AI Recruiter Analysis"
        )

        recruiter = (
            profile_data[
                "recruiter_analysis"
            ]
        )

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                "Recommended Roles"
            )

            for role in recruiter[
                "recommended_roles"
            ]:

                st.success(role)

        with col2:

            st.write("Strengths")

            for strength in recruiter[
                "strengths"
            ]:

                st.info(strength)

        st.write("Weaknesses")

        for weakness in recruiter[
            "weaknesses"
        ]:

            st.warning(weakness)

        st.markdown("---")

        render_dna_section(

            profile_data[
                "developer_dna"
            ]
        )

        st.markdown("---")

        render_startup_section(

            profile_data[
                "startup_readiness"
            ]
        )

        st.markdown("---")

        render_wrapped_section(
            wrapped_data
        )

        st.markdown("---")

        st.subheader(
            "AI Resume Generator"
        )

        if resume_data:

            resume_markdown = (
                resume_data[
                    "markdown_resume"
                ]
            )

            st.download_button(

                label=
                    "Download Resume",

                data=resume_markdown,

                file_name=(
                    f"{username}_resume.md"
                ),

                mime="text/markdown"
            )

            with st.expander(
                "Preview Resume"
            ):

                st.markdown(
                    resume_markdown
                )

        st.markdown("---")

        st.subheader(
            "Repositories"
        )

        repositories = pd.DataFrame(

            profile_data[
                "repositories"
            ]
        )

        repositories = (
            repositories.sort_values(

                by="stars",

                ascending=False
            )
        )

        st.dataframe(
            repositories,
            use_container_width=True
        )