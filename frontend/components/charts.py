import plotly.express as px
import pandas as pd
import streamlit as st


def render_language_chart(
    language_stats
):

    dataframe = pd.DataFrame({

        "Language":
            list(language_stats.keys()),

        "Count":
            list(language_stats.values())
    })

    figure = px.bar(

        dataframe,

        x="Language",

        y="Count",

        title="Technology Usage",

        text_auto=True
    )

    figure.update_layout(

        xaxis_title="Technology",

        yaxis_title="Repositories",

        height=500
    )

    st.plotly_chart(

        figure,

        use_container_width=True
    )