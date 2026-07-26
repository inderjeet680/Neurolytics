import streamlit as st
import pandas as pd

from modules.data_cleaner import analyze_dataset


def show():

    st.title("🧹 Data Cleaning")

    if "dataset" not in st.session_state:
        st.warning("Please upload a dataset first.")
        return

    df = st.session_state["dataset"]

    report = analyze_dataset(df)

    col1, col2 = st.columns(2)

    col1.metric(
        "Missing Values",
        report["total_missing"]
    )

    col2.metric(
        "Duplicate Rows",
        report["duplicate_rows"]
    )

    st.divider()

    st.subheader("Missing Values by Column")

    missing_df = pd.DataFrame({
        "Column": report["missing_by_column"].keys(),
        "Missing Values": report["missing_by_column"].values(),
        "Missing %": report["missing_percentage"].values()
    })

    st.dataframe(
        missing_df,
        use_container_width=True
    )

    st.divider()

    st.subheader("Data Types")

    dtype_df = pd.DataFrame({
        "Column": report["data_types"].keys(),
        "Data Type": report["data_types"].values()
    })

    st.dataframe(
        dtype_df,
        use_container_width=True
    )