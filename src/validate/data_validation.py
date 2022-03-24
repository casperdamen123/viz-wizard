from src.utils.get_data import get_number_of_numeric_columns
from src.exceptions import MissingMinimumAmountNumericColumns
import pandas as pd
import streamlit as st


class DataValidation:
    """Validate the uploaded data to check minimum visualization requirements"""
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.num_numeric_columns = 3

    def validate_data(self):
        """Checks all data requirement for uploaded data
        Returns:
            result (bool): True if all checks passed, else False
        """
        validations = []
        if self.df is not None:
            validations.append(self._check_numeric_columns(df=self.df, n=self.num_numeric_columns))

        validation_result = all(validations)
        return validation_result

    @staticmethod
    def _check_numeric_columns(df: pd.DataFrame, n: int) -> bool:
        """Checks whether the amount of numeric columns is meeting the minimal requirement
        Args:
            df (pd.DataFrame): Dataframe with uploaded data
        Return:
            result (bool): True if check passed, else False
        """
        result = get_number_of_numeric_columns(df) >= n
        if not result:
            raise MissingMinimumAmountNumericColumns(st.info(f'Found {get_number_of_numeric_columns(df)} numeric \
                                                               columns but the wizard needs at least {n} numeric \
                                                               columns. Please upload a new file'
                                                             )
                                                     )
        return result
