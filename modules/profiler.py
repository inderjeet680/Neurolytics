"""
Module: Dataset Profiler
Project: Neurolytics
"""

import pandas as pd


def profile_dataset(df: pd.DataFrame) -> dict:
    """
    Generate dataset profile information.
    """

    profile = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "memory_usage": round(df.memory_usage(deep=True).sum() / 1024, 2),

        "numeric_columns": df.select_dtypes(include=["number"]).columns.tolist(),

        "categorical_columns": df.select_dtypes(include=["object", "category"]).columns.tolist(),

        "datetime_columns": df.select_dtypes(include=["datetime"]).columns.tolist(),

        "boolean_columns": df.select_dtypes(include=["bool"]).columns.tolist(),

        "data_types": df.dtypes.astype(str).to_dict(),

        "unique_values": df.nunique().to_dict()
    }

    return profile