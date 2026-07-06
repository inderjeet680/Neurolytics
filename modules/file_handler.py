"""
Module: File Handler
Project: Neurolytics
"""

import pandas as pd


def load_dataset(uploaded_file):
    """
    Load CSV or Excel file into a Pandas DataFrame.
    """

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    elif uploaded_file.name.endswith((".xlsx", ".xls")):
        df = pd.read_excel(uploaded_file)

    else:
        raise ValueError("Unsupported file format.")

    return df


def get_file_info(df):
    """
    Return basic dataset information.
    """

    info = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "memory_usage": round(df.memory_usage(deep=True).sum() / 1024, 2)
    }

    return info