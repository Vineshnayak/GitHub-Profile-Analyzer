import streamlit as st


def render_profile_cards(profile):

    followers = profile["followers"]

    following = profile["following"]

    repositories = (
        profile["public_repos"]
    )

    col1, col2, col3 = (
        st.columns(3)
    )

    with col1:

        st.metric(
            "Followers",
            followers
        )

    with col2:

        st.metric(
            "Following",
            following
        )

    with col3:

        st.metric(
            "Repositories",
            repositories
        )