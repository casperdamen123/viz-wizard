import streamlit as st
import pandas as pd


class FileLoader:

    def read_as_dataframe(self) -> pd.DataFrame:

        uploaded_file = st.file_uploader("Upload your data file ↓", type=['csv', 'xlsx', 'txt'])

        if uploaded_file is not None:
            st.write(f"Preview:")

            try:

                if uploaded_file.type == 'text/csv':
                    df = self._read_csv(uploaded_file)
                    st.write(df.head())
                    return df

                elif uploaded_file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                    df = self._read_excel(uploaded_file)
                    st.write(df.head())
                    return df

                elif uploaded_file.type == 'text/plain':
                    df = self._read_text(uploaded_file)
                    st.write(df.head())
                    return df

            except Exception as e:
                st.info(e)

    def _read_csv(self, uploaded_file: st.file_uploader) -> pd.DataFrame:
        return pd.read_csv(uploaded_file)

    def _read_excel(self, uploaded_file: st.file_uploader) -> pd.DataFrame:
        return pd.read_excel(uploaded_file)

    def _read_text(self, uploaded_file: st.file_uploader) -> pd.DataFrame:
        return pd.read_table(uploaded_file)
