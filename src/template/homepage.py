import streamlit as st
from pathlib import Path
from PIL import Image


class HomePageSetup:
    """Sets up template template for the homepage with elements shown upon initial page load"""
    def setup_home(self):

        self._set_title()
        self._set_images()
        self._set_header()

    @staticmethod
    def _set_title():
        """Configure main title"""
        st.title("Welcome to the Viz Wizard!")

    @staticmethod
    def _set_images():
        """Set main images"""
        wiz_image = Image.open(Path(__file__).parents[1] / 'images/wizard.png')
        chart_image = Image.open(Path(__file__).parents[1] / 'images/charts.jpeg')

        st.image([wiz_image, chart_image], width=352)

    @staticmethod
    def _set_header():
        """Configure sub title"""
        st.subheader("Drop your data and let us do the Viz magic")
