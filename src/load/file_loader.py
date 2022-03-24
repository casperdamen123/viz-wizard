import streamlit as st
import pandas as pd
from src.exceptions import FileLoaderError


class FileLoader:
    """Implementation to handle the raw data file upload"""

    def __init__(self):
        self.data_types = ['csv', 'xlsx', 'txt']
        self.separators = ['Make Selection', 'n/a', ',', ';']
        self.uploaded_file = self._file_uploader()

    def read_as_dataframe(self) -> pd.DataFrame:
        """Reads the raw data file and transforms this to a dataframe.
        Returns:
            df (pd.DataFrame): Dataframe with raw data uploaded
            status (bool): Indicates if the data is loaded correctly
        """

        if self.uploaded_file is not None:

            # Load data
            if self.uploaded_file.type == 'text/csv':
                df = self._read_csv(self.uploaded_file)
                self._preview_data(df)
                return df

            elif self.uploaded_file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                df= self._read_xlsx(self.uploaded_file)
                self._preview_data(df)
                return df

            elif self.uploaded_file.type == 'text/plain':
                df = self._read_txt(self.uploaded_file)
                self._preview_data(df)
                return df

    def _file_uploader(self) -> st.file_uploader:
        """Create uploader for raw data files
        Returns:
            uploaded_file (st.file_uploader): Uploaded file
        """
        uploaded_file = st.file_uploader("Upload your data file ↓", type=self.data_types)
        return uploaded_file

    @staticmethod
    def _read_csv(uploaded_file: st.file_uploader) -> pd.DataFrame:
        """Reads csv file as dataframe
        Args:
            uploaded_file: File in csv format
        Returns:
            df (pd.DataFrame): Dataframe with raw uploaded data
        """
        try:
            df = pd.read_csv(uploaded_file)
            return df
        except Exception as e:
            raise FileLoaderError(st.info(f"Unable to load raw data, please try again. Error message: \n {e}"))

    @staticmethod
    def _read_xlsx(uploaded_file: st.file_uploader) -> pd.DataFrame:
        """Reads xlsx file as dataframe
        Args:
            uploaded_file: File in xlsx format
        Returns:
            df (pd.DataFrame): Dataframe with raw uploaded data
        """
        try:
            df = pd.read_excel(uploaded_file)
            return df
        except Exception as e:
            raise FileLoaderError(st.info(f"Unable to load raw data, please try again. Error message: \n {e}"))

    @staticmethod
    def _read_txt(uploaded_file: st.file_uploader) -> pd.DataFrame:
        """Reads txt file as dataframe
        Args:
            uploaded_file: File in txt format
        Returns:
            df (pd.DataFrame): Dataframe with raw uploaded data
        """
        try:
            df = pd.read_table(uploaded_file)
            return df
        except Exception as e:
            raise FileLoaderError(st.info(f"Unable to load raw data, please try again. Error message: \n {e}"))

    @staticmethod
    def _preview_data(df: pd.DataFrame):
        """Show first rows of raw uploaded data
        Args:
            df: Dataframe with raw uploaded data
        Returns:
            None
        """
        st.write(f"Data Preview:")
        st.write(df.head())
        st.info("Not happy with the format? Validate the format of your raw file and re-upload! \
                 Make sure to use comma separation when uploading a CSV file!")
