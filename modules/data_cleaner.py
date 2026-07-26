"""
Module: Data Cleaner
Project: Neurolytics
"""

import pandas as pd


def analyze_dataset(df: pd.DataFrame) -> dict:

    missing = df.isnull().sum()

    report = {
        "total_missing": int(missing.sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_by_column": missing.to_dict(),
        "missing_percentage": (
            (missing / len(df)) * 100
        ).round(2).to_dict(),
        "data_types": df.dtypes.astype(str).to_dict()
    }

    return report