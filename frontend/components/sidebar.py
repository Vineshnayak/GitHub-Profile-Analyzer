import streamlit as st


def render_sidebar():

    st.sidebar.title(
        "GitHub Profile Analyzer"
    )

    st.sidebar.markdown(
        "---"
    )

    username = st.sidebar.text_input(
        "GitHub Username"
    )

    analyze_button = (
        st.sidebar.button(
            "Analyze Profile",
            use_container_width=True
        )
    )

    st.sidebar.markdown(
        "---"
    )

    st.sidebar.info(
        "AI-powered GitHub analytics "
        "platform using FastAPI "
        "and Streamlit."
    )

    return username, analyze_button