"""
Module: Dataset Profiler
Project: Neurolytics
"""

import pandas as pd


def detect_date_columns(df: pd.DataFrame) -> list:
    """
    Detect columns that contain date values but are stored as
    object/string data types.
    """

    detected_dates = []

    for column in df.columns:

        # Only check string/object columns
        if df[column].dtype == "object":

            try:
                sample = df[column].dropna().head(50)

                # Skip completely empty columns
                if len(sample) == 0:
                    continue

                # Try converting sample values to datetime
                pd.to_datetime(sample, errors="raise")

                detected_dates.append(column)

            except (ValueError, TypeError):
                continue

    return detected_dates


def profile_dataset(df: pd.DataFrame) -> dict:
    """
    Generate complete dataset profile information.
    """

    profile = {
        # Basic information
        "rows": df.shape[0],
        "columns": df.shape[1],

        # Data quality
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),

        # Memory
        "memory_usage": round(
            df.memory_usage(deep=True).sum() / 1024,
            2
        ),

        # Column categories
        "numeric_columns": df.select_dtypes(
            include=["number"]
        ).columns.tolist(),

        "categorical_columns": df.select_dtypes(
            include=["object", "category"]
        ).columns.tolist(),

        "datetime_columns": df.select_dtypes(
            include=["datetime"]
        ).columns.tolist(),

        "boolean_columns": df.select_dtypes(
            include=["bool"]
        ).columns.tolist(),

        # Detailed information
        "data_types": df.dtypes.astype(str).to_dict(),

        "unique_values": df.nunique().to_dict(),

        # Auto date detection
        "detected_date_columns": detect_date_columns(df)
    }

    return profile