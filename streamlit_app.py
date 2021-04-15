  
# streamlist_app.py
# Streamlit application.
#
# Abby Vorhaus, Jeff Moore, Kyle Dotterrer, Will Borom

import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_timeline import timeline
import psw


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
    st.markdown("<h1 style='text-align: center; color: " + COLOR_SCHEME_BLUE + ";'>Machine Superintelligence</h1>", unsafe_allow_html=True)
    '''
    
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

    path = DATA_PATH + TIMELINE_DATA_FILENAME
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
    #read in data as csv
    COUNTRY_VOTES =  pd.read_csv("data/CountryVotesonAI.csv")
    #combine totally agree/tend agree to one agree column for user clarity
    COUNTRY_VOTES["Agree"] = COUNTRY_VOTES["Tend_Agree"] + COUNTRY_VOTES["Totally_Agree"]
    #combine totally disagree/tend disagree to one disagree column for user clarity
    COUNTRY_VOTES["Disagree"] = COUNTRY_VOTES["Tend_Disagree"] + COUNTRY_VOTES["Totally_Disagree"]
    COUNTRY_VOTES = COUNTRY_VOTES.rename(columns={"Totally_Agree": "Totally Agree", "Tend_Agree": "Tend Agree", "Tend_Disagree": "Tend Disagree", "Totally_Disagree": "Totally Disagree"})

    country_selector = alt.selection_multi(fields=['Country'], init=[{'Country':'Hungary'}])
    
    #transform fold is conducted so that we can utilize the stacked bar approach
    #and analyze the huge discrepanacy between what world powers think
    '''
    ## World Power Believe on AI Safety and Regulation
    '''

    all_country_data = alt.Chart(COUNTRY_VOTES).mark_bar().encode(
        x=alt.X('Agree:Q', title="Percent Representatives that Want AI Regulation", scale=alt.Scale(domain=[0, 100])),
        y=alt.Y('Country:N', title="Country"), 
        color=alt.condition(country_selector, alt.value('#714141'), alt.value('#d9d9d9'))
    ).add_selection(
        country_selector
    ).interactive()


    by_country2 = alt.Chart(COUNTRY_VOTES).transform_fold(
        ['Agree', 'Disagree'],
        as_=['Sentiment', 'Agree/Disagree']
    ).mark_bar().encode(
        x=alt.X('Country:N', title='Country'),
        y=alt.Y('Agree/Disagree:Q', title='Is AI Regulation Needed?', scale=alt.Scale(domain=[0, 100])),
        tooltip=[alt.Tooltip("Country:N", title='Country')], 
        color=alt.Color('Sentiment:N',
            scale = alt.Scale(domain=['Agree', 'Disagree'], range=['#714141', '#d9d9de'])
        )
    ).transform_filter(
        country_selector
    ).interactive()

    joint_chart = all_country_data | by_country2



    st.write(joint_chart)
    st.write("From the chart above we can see that nearly every major world power agrees" +
    " that AI imposes enough risk that it should be regulated. There is not one outlier nation " +
    "that does not think that AI and Robotics are begning to play in increasingly " +
    "dangerous or volatile role.")


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
    '''
    ## What is the view of Artificial Intelligence in the media?  
    The following word cloud expresses some of the sentiment that can be seen in recent articles about AI.
    '''
    articleData = psw.getData("data/articles.json")
    articleText = psw.buildWordCloudText(articleData)
    wc = psw.getWordCloud(articleText)
    st.write(wc)
    '''
    The table below shows a document level sentiment analysis of each of the articles that were pulled from Google today.  
    As you can see there is mostly positive sentiment associated with AI from the articles.
    '''
    finalSent = pd.read_csv("data/sentiment.csv")
    sentChart = psw.buildChart(finalSent)
    st.write(sentChart)



# -----------------------------------------------------------------------------
# Chapter: What Would You Choose
# -----------------------------------------------------------------------------

def user_selection():
    col1, col2, col3 = st.beta_columns([1,3,1])

    age_range = col2.radio("Choose your age bracket from the provided ranges.", ("-", "18 to 29", "30 to 44", "45 to 59", "60+"))   
    if age_range != "-":
        gender_at_birth = col2.radio("Choose your sex.", ("-", "Female", "Male"))
        if gender_at_birth != "-":
            odds = col2.radio("Choose the Odds. Remember, this is the chance that humanity will face complete destruction.", 
                ("-", "1 in 2", "1 in 3", "1 in 4", "1 in 5", "1 in 10")) 
            if odds != "-":
                yes_or_no = col2.radio("Given the odds, should we as humanity continue to pursue this advancement?", ("-", "Yes", "No"))
                if yes_or_no == "Yes":
                    st.write("cool bro")
                elif yes_or_no == "No":
                    st.write("Live to fight another day")

    


def render_user_choice():
    """
    Render chapter four user choice.
    """
    '''
    ---
    '''
    st.markdown("<h1 style='text-align: center; color: " + COLOR_SCHEME_BLUE + ";'>What Do You Choose?</h1>", unsafe_allow_html=True)

    '''
    
    In 2017 author Rick Webb wrote an article for NewCo Shift on machine superintelligence and public opinion. In the process of developing
    this article, he surveyed various populations in the United States. One of the questions posed was "Humanity has discovered a scientific advancement. 
    Pursuing it gives humanity two possible options: a chance that all of humanity will die instantly, or a chance that poverty, death and disease 
    will be cured for everyone, forever. Should we pursue it?

    In his survey, Webb put the chance at varying levels to see how the public would respond, but the two results, transcendence or destruction, were always the same. 
    Now, we will give you a chance to do the same and see how you compare to the rest of the respondents.

    First select your age range and sex. This will let you see how you compare amongst others. Don't worry! You can use the sidebar
    later to explore further and compare across different ages and genders as well as look at how different regions across the United States
    differ in opinion. As a note, the survey only provided the option for male or female so we unfortunately do not have data for other options at this time.

    Next, select one of the odds. The odds represent the chance that humanity will be destroyed. For example, 1 in 3 implies that one out
    of every three times, humanity will be completely and totally annihilated by the advancement we achieved. However, the other two times the
    result will be a world with no famine, disease, poverty, suffering, or death - in short a utopia. You decide whether we should continue down the
    path or not.

    '''
    #
    
    #Set up the Radio Button Theme
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.write('<style>div.row-widget.stRadio > div[role="radiogroup"] > label[data-baseweb="radio"] > div:first-child {background-color:'
        + COLOR_SCHEME_BLUE + '};</style>', unsafe_allow_html=True)
    st.markdown(
    """ <style>
            div[role="radiogroup"] >  :first-child{
                display: none !important;
            } 
        </style> """, unsafe_allow_html=True)

    #let the use choose their fate
    user_selection()

    #SideBar
    


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
    
    # Chapter 4: What would you choose?
    render_user_choice()

    render_conclusion_content()

    render_references()

# -----------------------------------------------------------------------------
# Application Entry Point
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
