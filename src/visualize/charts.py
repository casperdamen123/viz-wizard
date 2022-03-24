from src.utils.get_data import get_numeric_data, get_random_columns_df, get_random_columns_str
import pandas as pd
import streamlit as st
import numpy as np
import altair as alt
from typing import List, Union


class DataViz:
    """Generate random visualizations using raw data file"""
    def __init__(self, df):
        self.df = df

    def show_random_viz(self):
        """Main process to create or change viz on button click"""
        # TO DO: Add functionality to keep history of chosen viz
        if self.df is not None:
            self._button_random_viz()
            self._format_viz_button()
            if self.button:
                self._generate_random_viz()

    def _button_random_viz(self) -> st.button:
        """Button to click for viz generation"""
        self.button = st.button('Click here to use Viz Magic on this dataset!')
        return self.button

    def _generate_random_viz(self) -> Union[st.plotly_chart, st.bar_chart, st.area_chart]:
        """Pick random viz from pre-defined options
        Returns:
            viz: Randomly chosen viz
        """
        viz_magic = [self._line_plot, self._bar_plot, self._area_plot, self._scatter_chart]
        viz_pick = viz_magic[np.random.randint(0, len(viz_magic))]
        return viz_pick(self.df)

    @staticmethod
    def _line_plot(df: pd.DataFrame) -> st.line_chart:
        """Generate line plot
        Args:
            df (pd.DataFrame): Dataframe to use for viz
        Returns:
            viz (st.line_chart): Streamlit line chart
        """
        num_df = get_numeric_data(df)
        viz = st.line_chart(get_random_columns_df(num_df, 3))
        return viz

    @staticmethod
    def _bar_plot(df: pd.DataFrame) -> st.bar_chart:
        """Generate bar plot
        Args:
            df (pd.DataFrame): Dataframe to use for viz
        Returns:
            viz (st.bar_chart): Streamlit bar chart
        """
        num_df = get_numeric_data(df)
        viz = st.bar_chart(get_random_columns_df(num_df, 3))
        return viz

    @staticmethod
    def _area_plot(df: pd.DataFrame) -> st.area_chart:
        """Generate area plot
        Args:
            df (pd.DataFrame): Dataframe to use for viz
        Returns:
            viz (st.area_chart): Streamlit area chart
        """
        num_df = get_numeric_data(df)
        viz = st.area_chart(get_random_columns_df(num_df, 3))
        return viz

    @staticmethod
    def _scatter_chart(df: pd.DataFrame) -> st.altair_chart:
        """Generate scatter plot
        Args:
            df (pd.DataFrame): Dataframe to use for viz
        Returns:
            viz (st.altair_chart): Scatter plot using altair
        """
        num_df = get_numeric_data(df)
        cols = get_random_columns_str(num_df, 3)
        scatter = alt.Chart(num_df).mark_point().encode(x=cols[0], y=cols[1], color=cols[2]).interactive()
        viz = st.altair_chart(scatter, use_container_width=True)
        return viz

    @staticmethod
    def _format_viz_button():
        """Format the button to generate visualizations"""
        st.write("##")
        st.markdown("""
                    <style>
                    div.stButton > button:first-child {
                        border-color: #ffffff;
                    }
                    </style>""", unsafe_allow_html=True
                    )
