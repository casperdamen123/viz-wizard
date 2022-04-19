from src.utils.get_data import (
    get_numeric_data,
    get_text_data,
    get_numeric_and_text_df,
    get_random_columns_df,
    get_random_columns_str
)

from src.logger.event_logging import EventLogging
import pandas as pd
import streamlit as st
import altair as alt
from typing import Union
import plotly.express as px
import random


class DataViz:
    """Generate random visualizations using raw data file"""

    def __init__(self, df):
        self.df = df
        #self.logging = EventLogging()

    def show_random_viz(self):
        """Main process to create or change viz on button click"""
        if self.df is not None:
            self._button_random_viz()
            self._format_viz_button()
            if self.button:
                self._generate_random_viz()

    def _button_random_viz(self) -> st.button:
        """Button to click for viz generation"""
        st.write("")
        st.write("")
        col1, col2, col3 = st.columns([1, 1, 1])
        self.button = col2.button('Click here to use Viz Magic!')
        return self.button

    def _generate_random_viz(self) -> Union[st.plotly_chart, st.bar_chart, st.area_chart,
                                            st.altair_chart, st.line_chart]:
        """Pick random viz from pre-defined options
        Returns:
            viz: Randomly chosen viz
        """
        viz_magic = [self._line_plot, self._bar_plot, self._hor_bar_plot, self._stack_bar_plot,
                     self._area_plot, self._scatter_chart, self._boxplot_chart, self._donut_chart,
                     self._bubble_chart]

        viz_pick = random.choice(viz_magic)

        #self.logging.log_generated_charts(viz_pick.__name__.replace('_', ''))
        return viz_pick(self.df)

    @staticmethod
    def _format_viz_button():
        """Format the button to generate visualizations"""
        st.markdown("""
                    <style>
                    div.stButton > button:first-child {
                        border-color: #00FF00;
                    }
                    div.stButton > button:hover {
                        color: #00FF00;
                    }
                    </style>""", unsafe_allow_html=True
                    )

    # Start Chart magic

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
        """Generate vertical bar plot
        Args:
            df (pd.DataFrame): Dataframe to use for viz
        Returns:
            viz (st.bar_chart): Streamlit bar chart
        """
        num_df = get_numeric_data(df)
        viz = st.bar_chart(get_random_columns_df(num_df, 3))
        return viz

    @staticmethod
    def _hor_bar_plot(df: pd.DataFrame) -> st.altair_chart:
        """Generate horizontal bar plot
        Args:
            df (pd.DataFrame): Dataframe to use for viz
        Returns:
            viz (st.altair_chart): Altair bar chart
        """
        num_df = get_numeric_data(df)
        cols = get_random_columns_str(num_df, 2)
        hor_bar = alt.Chart(df).mark_bar().encode(x=cols[0], y=cols[1])
        viz = st.altair_chart(hor_bar, use_container_width=True)
        return viz

    @staticmethod
    def _stack_bar_plot(df: pd.DataFrame) -> st.altair_chart:
        """Stacked bar plot
        Args:
            df (pd.DataFrame): Dataframe to use for viz
        Returns:
            viz (st.altair_chart): Altair stacked bar chart
        """
        num_text_df = get_numeric_and_text_df(df)
        num_cols = get_random_columns_str(num_text_df, 1)
        text_cols = get_random_columns_str(num_text_df, 2)
        stack_bar = alt.Chart(num_text_df).mark_bar().encode(
            x=text_cols[0],
            y=num_cols[0],
            color=text_cols[1]
        )
        viz = st.altair_chart(stack_bar, use_container_width=True)
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
        scatter = alt.Chart(num_df).mark_point().encode(x=cols[0], y=cols[1], color=cols[2])
        viz = st.altair_chart(scatter, use_container_width=True)
        return viz

    @staticmethod
    def _boxplot_chart(df: pd.DataFrame) -> st.altair_chart:
        """Generate boxplot
        Args:
            df (pd.DataFrame): Dataframe to use for viz
        Returns:
            viz (st.altair_chart): Boxplot using altair
        """
        num_df = get_numeric_data(df)
        cols = get_random_columns_str(num_df, 2)
        boxplot = alt.Chart(num_df).mark_point().encode(x=cols[0], y=cols[1])
        viz = st.altair_chart(boxplot, use_container_width=True)
        return viz

    @staticmethod
    def _donut_chart(df: pd.DataFrame) -> st.plotly_chart:
        """Generate donut plot
        Args:
            df (pd.DataFrame): Dataframe to use for viz
        Returns:
            viz (st.plotly_chart): Donut chart using plotly
        """
        num_df = get_numeric_data(df)
        num_data = get_random_columns_df(num_df, 1).unique()
        text_df = get_text_data(df)
        text_data = get_random_columns_df(text_df, 1).unique()
        fig = px.pie(hole=0.2, labels=num_data, names=text_data)
        viz = st.plotly_chart(fig)
        return viz

    @staticmethod
    def _bubble_chart(df: pd.DataFrame) -> st.plotly_chart:
        """Generate donut plot
        Args:
            df (pd.DataFrame): Dataframe to use for viz
        Returns:
            viz (st.plotly_chart): Donut chart using plotly
        """
        num_text_df = get_numeric_and_text_df(df)
        num_cols = get_random_columns_str(num_text_df, 3)
        text_cols = get_random_columns_str(num_text_df, 2)
        bubble = px.scatter(data_frame=num_text_df, x=num_cols[0], y=num_cols[1],
                            size=num_cols[2], color=text_cols[0], hover_name=text_cols[1],
                            size_max=20)
        viz = st.plotly_chart(bubble)
        return viz
