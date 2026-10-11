import pandas as pd


def missing_value_audit(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes missing value counts and percentages for each feature.
    """
    missing = df.isnull().sum()
    missing_percent = (missing / len(df)) * 100

    audit_df = pd.DataFrame({"Missing Values": missing, "Percentage (%)": missing_percent}).sort_values(
        by="Percentage (%)", ascending=False
    )

    return audit_df[audit_df["Missing Values"] > 0]


def summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generates standard descriptive statistics for numerical columns.
    """
    return df.describe().T
