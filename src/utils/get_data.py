import random
import pandas as pd
from typing import List


def get_random_columns_str(df: pd.DataFrame, n: int) -> List[str]:
    """Select random column names from df
    Args:
        df (pd.Dataframe): Original dataframe
        n (int): Number of columns names to get
    Returns:
        columns (List[str]): List with column names
    """
    columns = random.sample(df.columns.tolist(), n)
    return columns


def get_random_columns_df(df: pd.DataFrame, n: int) -> pd.DataFrame:
    """Select random columns from df
    Args:
        df (pd.Dataframe): Original dataframe
        n (int): Number of columns to get
    Returns:
        df (pd.Dataframe): Dataframe with randomly chosen data columns
    """
    columns = random.sample(df.columns.tolist(), n)
    if n == 1:
        columns = columns[0]
    return df[columns]


def get_numeric_data(df: pd.DataFrame) -> pd.DataFrame:
    """Get numeric columns from dataframe
    Args:
        df (pd.DataFrame): Dataframe with all data
    Returns:
        num_df (pd.DataFrame): Dataframe with only numeric columns
    """
    num_df = df.select_dtypes(include='number')
    return num_df


def get_number_of_numeric_columns(df: pd.DataFrame) -> int:
    """Get the number of numeric columns from dataframe
    Args:
        df (pd.Dataframe): Original dataframe
    Returns:
        length (int): Number of numeric columns
    """
    data = get_numeric_data(df)
    length = len(data.columns)
    return length


def get_text_data(df: pd.DataFrame) -> pd.DataFrame:
    """Get text columns from dataframe
    Args:
        df (pd.DataFrame): Dataframe with all data
    Returns:
        text_df (pd.DataFrame): Dataframe with only text columns
    """
    text_df = df.select_dtypes(include='object')
    return text_df


def get_number_of_text_columns(df: pd.DataFrame) -> int:
    """Get the number of numeric columns from dataframe
    Args:
        df (pd.Dataframe): Original dataframe
    Returns:
        length (int): Number of text columns
    """
    data = get_text_data(df)
    length = len(data.columns)
    return length


def get_numeric_and_text_df(df: pd.DataFrame):
    """Get numeric and text columns from dataframe
    Args:
        df (pd.DataFrame): Dataframe with all data
    Returns:
        num_text_df (pd.DataFrame): Dataframe with only text and numeric columns
    """
    num_text_df = df.select_dtypes(include=['number', 'object'])
    return num_text_df
