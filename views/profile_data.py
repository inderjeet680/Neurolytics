"""
Module: Dataset Profile View
Project: Neurolytics
"""

import streamlit as st
import pandas as pd

from modules.profiler import profile_dataset


def show():

    st.title("📑 Dataset Profile")

    # Check if dataset exists
    if "dataset" not in st.session_state:

        st.warning(
            "Please upload a dataset first."
        )

        return

    df = st.session_state["dataset"]

    # Generate profile
    profile = profile_dataset(df)

    # -----------------------------------
    # BASIC INFORMATION
    # -----------------------------------

    st.subheader("📊 Dataset Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Rows",
            profile["rows"]
        )

    with col2:
        st.metric(
            "Columns",
            profile["columns"]
        )

    with col3:
        st.metric(
            "Memory (KB)",
            profile["memory_usage"]
        )

    # -----------------------------------
    # DATA QUALITY
    # -----------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Missing Values",
            profile["missing_values"]
        )

    with col2:
        st.metric(
            "Duplicate Rows",
            profile["duplicate_rows"]
        )

    with col3:
        st.metric(
            "Numeric Columns",
            len(profile["numeric_columns"])
        )

    st.divider()

    # -----------------------------------
    # COLUMN CATEGORIES
    # -----------------------------------

    st.subheader("🔍 Column Categories")

    col1, col2 = st.columns(2)

    with col1:

        st.write("### 🔢 Numeric Columns")

        if profile["numeric_columns"]:
            st.write(profile["numeric_columns"])
        else:
            st.info("No numeric columns found.")

        st.write("### 🔘 Boolean Columns")

        if profile["boolean_columns"]:
            st.write(profile["boolean_columns"])
        else:
            st.info("No boolean columns found.")

    with col2:

        st.write("### 🏷️ Categorical Columns")

        if profile["categorical_columns"]:
            st.write(profile["categorical_columns"])
        else:
            st.info("No categorical columns found.")

        st.write("### 📅 Datetime Columns")

        if profile["datetime_columns"]:
            st.write(profile["datetime_columns"])
        else:
            st.info("No datetime columns found.")

    st.divider()

    # -----------------------------------
    # AUTO DATE DETECTION
    # -----------------------------------

    st.subheader("🤖 Auto Date Detection")

    detected_dates = profile["detected_date_columns"]

    if detected_dates:

        st.success(
            f"Potential date columns detected: {len(detected_dates)}"
        )

        for column in detected_dates:

            st.write(
                f"📅 **{column}**"
            )

        st.info(
            "These columns appear to contain date values "
            "but are currently stored as text."
        )

    else:

        st.info(
            "No additional date columns detected."
        )

    st.divider()

    # -----------------------------------
    # DATA TYPES
    # -----------------------------------

    st.subheader("🧬 Data Types")

    dtype_df = pd.DataFrame(
        {
            "Column": profile["data_types"].keys(),
            "Data Type": profile["data_types"].values()
        }
    )

    st.dataframe(
        dtype_df,
        use_container_width=True,
        hide_index=True
    )

    # -----------------------------------
    # UNIQUE VALUES
    # -----------------------------------

    st.subheader("🔢 Unique Values")

    unique_df = pd.DataFrame(
        {
            "Column": profile["unique_values"].keys(),
            "Unique Values": profile["unique_values"].values()
        }
    )

    st.dataframe(
        unique_df,
        use_container_width=True,
        hide_index=True
    )