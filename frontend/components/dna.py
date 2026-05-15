import streamlit as st


def render_dna_section(
    dna_data
):

    st.subheader(
        "Developer DNA"
    )

    st.success(

        f"Developer Type: "
        f"{dna_data['developer_type']}"
    )

    st.write("Traits")

    for trait in dna_data[
        "traits"
    ]:

        st.info(trait)