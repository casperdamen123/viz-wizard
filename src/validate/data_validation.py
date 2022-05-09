from src.utils.get_data import get_number_of_numeric_columns, get_number_of_text_columns
from src.exceptions import MissingMinimumAmountNumericColumns, MissingMinimumAmountTextColumns
import pandas as pd
import streamlit as st


class DataValidation:
    """Validate the uploaded data to check minimum visualization requirements"""
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.num_numeric_columns = 3
        self.num_text_columns = 2

    def validate_data(self):
        """Checks all data requirement for uploaded data
        Returns:
            result (bool): True if all checks passed, else False (raises exception in the process)
        """
        validations = []
        if self.df is not None:
            validations.append(self._check_numeric_columns(df=self.df, n=self.num_numeric_columns))
            validations.append(self._check_text_columns(df=self.df, n=self.num_text_columns))
            validation_result = all(validations)

        else:
            validation_result = False
            
        return validation_result

    @staticmethod
    def _check_numeric_columns(df: pd.DataFrame, n: int) -> bool:
        """Checks whether the amount of numeric columns is meeting the minimal requirement
        Args:
            df (pd.DataFrame): Dataframe with uploaded data
        Return:
            result (bool): True if check passed, else False
        """
        num_cols = get_number_of_numeric_columns(df)
        result = num_cols >= n
        if not result:
            raise MissingMinimumAmountNumericColumns(st.info(f'Found {num_cols} numeric columns but the wizard needs \
                                                               at least {n} numeric columns. Please upload a new file')
                                                     )
        return result

    @staticmethod
    def _check_text_columns(df: pd.DataFrame, n: int) -> bool:
        """Checks whether the amount of text columns is meeting the minimal requirement
        Args:
            df (pd.DataFrame): Dataframe with uploaded data
        Return:
            result (bool): True if check passed, else False
        """
        num_cols = get_number_of_text_columns(df)
        result = num_cols >= n
        if not result:
            raise MissingMinimumAmountTextColumns(st.info(f'Found {num_cols} text columns but the wizard \
                                                            needs at least {n} text columns. Please upload a new file')
                                                   )
        return result
