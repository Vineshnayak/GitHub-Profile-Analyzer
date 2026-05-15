import requests
import pandas as pd
import streamlit as st


# Backend API URL
API_URL = "https://github-profile-analyzer-3vy1.onrender.com/analyze"


# Streamlit page configuration
st.set_page_config(
    page_title="GitHub Profile Analyzer",
    page_icon="📊",
    layout="wide"
)


# Sidebar
st.sidebar.title("GitHub Profile Analyzer")

st.sidebar.info(
    """
    Analyze GitHub developer profiles,
    repositories, tech stacks,
    and developer activity.
    """
)


# App title
st.title("📊 GitHub Profile Analyzer")

st.write(
    "Analyze GitHub developer profiles professionally"
)


# Username input
username = st.text_input(
    "Enter GitHub Username"
)


# Analyze button
if st.button("Analyze Profile"):

    # Empty username validation
    if username.strip() == "":

        st.warning("Please enter a GitHub username")

    else:

        # Loading spinner
        with st.spinner("Analyzing GitHub profile..."):

            try:

                response = requests.get(
                    f"{API_URL}/{username}",
                    timeout=15
                )

                # Successful response
                if response.status_code == 200:

                    data = response.json()

                    st.success(
                        "Profile analyzed successfully"
                    )

                    # ---------------------------
                    # Profile Header
                    # ---------------------------

                    col1, col2 = st.columns([1, 4])

                    with col1:

                        st.image(
                            f"https://github.com/{username}.png",
                            width=150
                        )

                    with col2:

                        st.subheader(data["name"])

                        st.write(data["bio"])

                        github_url = (
                            f"https://github.com/{username}"
                        )

                        st.markdown(
                            f"[🔗 View GitHub Profile]"
                            f"({github_url})"
                        )

                    st.divider()

                    # ---------------------------
                    # Metrics Section
                    # ---------------------------

                    st.subheader(
                        "Developer Statistics"
                    )

                    metric1, metric2, metric3, metric4 = (
                        st.columns(4)
                    )

                    metric1.metric(
                        "Developer Score",
                        data["developer_score"]
                    )

                    metric2.metric(
                        "Followers",
                        data["followers"]
                    )

                    metric3.metric(
                        "Repositories",
                        data["public_repositories"]
                    )

                    metric4.metric(
                        "Total Stars",
                        data["total_stars"]
                    )

                    st.divider()

                    # ---------------------------
                    # Tech Stack
                    # ---------------------------

                    st.subheader("Tech Stack")

                    st.write(data["tech_stack"])

                    st.divider()

                    # ---------------------------
                    # Language Chart
                    # ---------------------------

                    st.subheader("Top Languages")

                    languages = data["top_languages"]

                    if languages:

                        language_df = pd.DataFrame({
                            "Language": list(
                                languages.keys()
                            ),
                            "Count": list(
                                languages.values()
                            )
                        })

                        language_df = (
                            language_df.set_index(
                                "Language"
                            )
                        )

                        st.bar_chart(language_df)

                    st.divider()

                    # ---------------------------
                    # Repository Table
                    # ---------------------------

                    st.subheader("Repositories")

                    repository_data = []

                    for repo in data["repositories"]:

                        repository_data.append({
                            "Repository":
                                f"https://github.com/"
                                f"{username}/"
                                f"{repo['name']}",

                            "Language":
                                repo["language"],

                            "Stars":
                                repo["stars"],

                            "Forks":
                                repo["forks"]
                        })

                    repo_df = pd.DataFrame(
                        repository_data
                    )

                    st.dataframe(
                        repo_df,
                        use_container_width=True,
                        hide_index=True
                    )

                else:

                    st.error(
                        "GitHub user not found"
                    )

            except requests.exceptions.Timeout:

                st.error(
                    "Request timed out. Try again."
                )

            except requests.exceptions.RequestException:

                st.error(
                    "Backend connection failed"
                )

            except Exception as error:

                st.error(
                    f"Unexpected error: {error}"
                )


st.divider()

st.caption(
    "Built using FastAPI, Streamlit, "
    "GitHub API, and GitHub Actions"
)
