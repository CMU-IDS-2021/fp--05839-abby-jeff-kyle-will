  
# streamlist_app.py
# Streamlit application.
#
# Abby Vorhaus, Jeff Moore, Kyle Dotterrer, Will Borom

import os
import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
from vega_datasets import data
from streamlit_timeline import timeline

# The relative path to the directory in which data is stored
DATA_PATH = "data/"

# The default height for our visualizations
DEFAULT_WIDTH = 800

# The default height for our visualizations
DEFAULT_HEIGHT = 550

# Colors from Vega color scheme for charts that should not be scaled
COLOR_SCHEME_BLUE = "#90c1dc"

# The name of the timeline data file
TIMELINE_DATA_FILENAME = "timeline.json"

# Allow streamlit to use the whole page
st.set_page_config(page_title="Artificial Intelligence", layout="wide")

# -----------------------------------------------------------------------------
# Introduction
# -----------------------------------------------------------------------------

def render_introduction_content():
    """
    Render the introduction content.
    """

    '''
    # Machine Superintelligence
    
    TODO: Compelling introduction content here.
    '''
    
    st.sidebar.header("Digging Deeper")
    st.sidebar.write(
        "We are only grazing the surface with our main graphics, " +
        "but you can keep exploring! Below you will find options " + 
        "for each section that will allow you to explore the data.")

# -----------------------------------------------------------------------------
# Chapter: History / Timeline
# -----------------------------------------------------------------------------

def render_history_chapter():
    """
    Render the history of artificial intelligence chapter.
    """

    '''
    # A Brief History of Artificial Intelligence

    Artificial intelligence may seem like a distinctly modern phenomenon, but research into the subject has been going on for nearly seventy years. Some of major milestones related to the development of machine superintelligence are highlighted in the timeline below.
    '''

    path = os.path.join(DATA_PATH, TIMELINE_DATA_FILENAME)
    with open(path, "r") as f:
        data = f.read()

    # Render the timeline
    timeline(data, height=500)

# -----------------------------------------------------------------------------
# Chapter: Terminator
# -----------------------------------------------------------------------------

def render_terminator_chapter():
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

def render_hal_chapter():
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
# References
# -----------------------------------------------------------------------------

def render_references():
    """
    Render the references for the project.
    """

    '''
    # References

    The works we referenced while working on this project are provided below.

    - McCarthy et al. _A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence._ 1955.
    '''

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def main():
    render_introduction_content()

    render_history_chapter()

    # Chapter 1: TODO
    render_terminator_chapter()

    # Chapter 2: TODO
    render_hal_chapter()

    render_conclusion_content()

    render_references()

# -----------------------------------------------------------------------------
# Application Entry Point
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
