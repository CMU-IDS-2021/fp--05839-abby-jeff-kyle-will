  
# streamlist_app.py
# Streamlit application.
#
# Abby Vorhaus, Jeff Moore, Kyle Dotterrer, Will Borom

import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
from vega_datasets import data

# The relative path to the directory in which data is stored
DATA_PATH = "data/"

# The default height for our visualizations
DEFAULT_WIDTH = 800

# The default height for our visualizations
DEFAULT_HEIGHT = 550

# Colors from Vega color scheme for charts that should not be scaled
COLOR_SCHEME_BLUE = "#90c1dc"

st.set_page_config(layout="wide")


# -----------------------------------------------------------------------------
# Introduction
# -----------------------------------------------------------------------------
def render_introduction_content():
    """
    Render the introduction content.
    """

    '''
    # Machine Super Intelligence
    
    ### The real reason we haven't heard from the aliens
    
    '''
    
    st.sidebar.header("Digging Deeper")
    st.sidebar.write(
        "We are only grazing the surface with our main graphics, " +
        "but you can keep exploring! Below you will find options " + 
        "for each section that will allow you to explore the data.")


# -----------------------------------------------------------------------------
# Chapter: Terminator
# -----------------------------------------------------------------------------

def render_chapter_one():
    """
    Render chapter one.
    """

    '''
    ---
    # Terminator 
    
    Hasta la vista baby.
    
    '''

# -----------------------------------------------------------------------------
# Chapter: HAL
# -----------------------------------------------------------------------------

def render_chapter_two():
    """
    Render chapter two.
    """

    '''
    ---
    # HAL 3000 
    
    I know that you and Frank were planning to disconnect me, and I'm afraid that's something I cannot allow to happen.
    
    '''

# -----------------------------------------------------------------------------
# Conclusion
# -----------------------------------------------------------------------------
def render_conclusion_content():
    """
    Render the conclusion content.
    """

    '''
    # Conclusion
    
    This concludes our exploration of the machine super intelligence! Don't worry, the machines already won.
    
    '''
    
  
# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def main():
    render_introduction_content()

    # Chapter 1: TODO
    render_chapter_one()

    # Chapter 2: TODO
    render_chapter_two()

    # ADD MORE CHAPTERS AS NEEDED

    render_conclusion_content()

# -----------------------------------------------------------------------------
# Application Entry Point
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
