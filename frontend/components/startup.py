import streamlit as st


def render_startup_section(
    startup_data
):

    st.subheader(
        "Startup Readiness"
    )

    st.metric(

        "Startup Readiness Score",

        startup_data[
            "startup_readiness_score"
        ]
    )

    deployment = (
        startup_data[
            "deployment_detected"
        ]
    )

    cicd = (
        startup_data[
            "ci_cd_detected"
        ]
    )

    st.write(
        f"Deployment Ready: "
        f"{deployment}"
    )

    st.write(
        f"CI/CD Ready: "
        f"{cicd}"
    )