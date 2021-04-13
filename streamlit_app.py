  
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

st.header("Here We Go")
