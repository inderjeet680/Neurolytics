import streamlit as st
from modules.profiler import profile_dataset


def show():

    st.title("📑 Dataset Profile")

    if "dataset" not in st.session_state:
        st.warning("Please upload a dataset first.")
        return

    df = st.session_state["dataset"]

    profile = profile_dataset(df)

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", profile["rows"])
    col2.metric("Columns", profile["columns"])
    col3.metric("Memory (KB)", profile["memory_usage"])

    col1, col2, col3 = st.columns(3)

    col1.metric("Missing Values", profile["missing_values"])
    col2.metric("Duplicate Rows", profile["duplicate_rows"])
    col3.metric("Numeric Columns", len(profile["numeric_columns"]))

    st.divider()

    st.subheader("Column Categories")

    col1, col2 = st.columns(2)

    with col1:
        st.write("### Numeric Columns")
        st.write(profile["numeric_columns"])

        st.write("### Boolean Columns")
        st.write(profile["boolean_columns"])

    with col2:
        st.write("### Categorical Columns")
        st.write(profile["categorical_columns"])

        st.write("### Datetime Columns")
        st.write(profile["datetime_columns"])

    st.divider()

    st.subheader("Data Types")

    st.dataframe(profile["data_types"])

    st.subheader("Unique Values")

    st.dataframe(profile["unique_values"])