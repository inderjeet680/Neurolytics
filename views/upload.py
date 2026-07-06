"""
Module: Upload Dataset
Project: Neurolytics
"""

import streamlit as st
import pandas as pd


def show():
    st.title("📂 Upload Dataset")

    uploaded_file = st.file_uploader(
        "Upload CSV or Excel File",
        type=["csv", "xlsx", "xls"]
    )

    if uploaded_file:

        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)

        else:
            df = pd.read_excel(uploaded_file)

        st.session_state["dataset"] = df

        st.success("Dataset Uploaded Successfully ✅")

        col1, col2, col3 = st.columns(3)

        col1.metric("Rows", df.shape[0])
        col2.metric("Columns", df.shape[1])
        col3.metric("Missing Values", int(df.isnull().sum().sum()))

        st.divider()

        st.subheader("Dataset Preview")

        st.dataframe(df.head(10), use_container_width=True)