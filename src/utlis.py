"""
Utility functions for the Stock Market Risk Analysis project.

These helper functions are used for basic stock industry classification
and saving output tables.
"""

import pandas as pd


def add_industry_info(df: pd.DataFrame, stock_column: str, industry_map: dict) -> pd.DataFrame:
    """
    Add industry code and industry name to a dataframe.

    Parameters:
        df: DataFrame containing stock identifiers
        stock_column: Column containing stock IDs
        industry_map: Dictionary mapping industry codes to industry names

    Returns:
        DataFrame with Industry_Code and Industry_Name columns
    """
    df = df.copy()
    df["Industry_Code"] = df[stock_column].str[0]
    df["Industry_Name"] = df["Industry_Code"].map(industry_map)
    return df


def save_table(df: pd.DataFrame, file_path: str) -> None:
    """
    Save a dataframe as a CSV file without index.
    """
    df.to_csv(file_path, index=False)