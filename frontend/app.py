import requests
import pandas as pd
import matplotlib          
matplotlib.use("Agg")      
import matplotlib.pyplot as plt
import streamlit as st


# Backend API URL
API_URL = "https://github-profile-analyzer-3vy1.onrender.com"

# Streamlit page settings
st.set_page_config(
    page_title="GitHub Profile Analyzer",
    layout="wide"
)

# Title
st.title("GitHub Profile Analyzer")

# Subtitle
st.write("Analyze GitHub developer profiles")

# Username input
username = st.text_input(
    "Enter GitHub Username"
)

# Analyze button
if st.button("Analyze Profile"):

    if username.strip() == "":
        st.warning("Please enter a username")

    else:

        # API request
        response = requests.get(
            f"{API_URL}/{username}"
        )

        # Success response
        if response.status_code == 200:

            data = response.json()

            # Top section
            st.header("Developer Overview")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Developer Score",
                data["developer_score"]
            )

            col2.metric(
                "Followers",
                data["followers"]
            )

            col3.metric(
                "Repositories",
                data["public_repositories"]
            )

            col4.metric(
                "Total Stars",
                data["total_stars"]
            )

            # Profile info
            st.subheader("Profile Information")

            st.write(f"Name: {data['name']}")
            st.write(f"Bio: {data['bio']}")

            # Tech stack
            st.subheader("Tech Stack")

            st.write(data["tech_stack"])

            # Language chart
            st.subheader("Top Languages")

            languages = data["top_languages"]

            if languages:

                language_names = list(languages.keys())
                language_counts = list(languages.values())

                fig, ax = plt.subplots()

                ax.bar(
                    language_names,
                    language_counts
                )

                ax.set_xlabel("Languages")
                ax.set_ylabel("Repository Count")

                st.pyplot(fig)

            # Repository table
            st.subheader("Repositories")

            repo_df = pd.DataFrame(
                data["repositories"]
            )

            st.dataframe(repo_df)

        else:
            st.error("GitHub user not found")