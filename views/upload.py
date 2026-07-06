import streamlit as st
from modules.file_handler import load_dataset, get_file_info


def show():

    st.title("📂 Upload Dataset")

    uploaded_file = st.file_uploader(
        "Upload CSV or Excel File",
        type=["csv", "xlsx", "xls"]
    )

    if uploaded_file:

        try:

            df = load_dataset(uploaded_file)

            st.session_state["dataset"] = df

            info = get_file_info(df)

            st.success("Dataset uploaded successfully ✅")

            col1, col2, col3 = st.columns(3)

            col1.metric("Rows", info["rows"])
            col2.metric("Columns", info["columns"])
            col3.metric("Missing", info["missing_values"])

            st.metric("Duplicate Rows", info["duplicate_rows"])
            st.metric("Memory (KB)", info["memory_usage"])

            st.divider()

            st.subheader("Dataset Preview")

            st.dataframe(df.head(10), use_container_width=True)

        except Exception as e:
            st.error(str(e))