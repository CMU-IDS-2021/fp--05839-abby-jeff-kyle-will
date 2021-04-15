  
# streamlist_app.py
# Streamlit application.
#
# Abby Vorhaus, Jeff Moore, Kyle Dotterrer, Will Borom

import psw
import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_timeline import timeline
import vega_datasets 


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
st.set_page_config(page_title="Machine Intelligence", layout="wide")

# -----------------------------------------------------------------------------
# Introduction
# -----------------------------------------------------------------------------

def render_introduction_content():
    """
    Render the introduction content.
    """

    '''
    # Machine Intelligence: Risks and Opportunities

    ---
    TODO: This introduction content can be far more compelling. 
    
    Machine intelligence is a complex topic - technically, socially, and ethically. Accordingly, navigating this topic requires a combination of both breadth and depth of understanding that is difficult to come by in most settings.

    In the following article, we seek to provide you with the tools to navigate this topic effectively. What is machine intelligence, and why is it important? What is our current position, and how did we get here? What are the likely future implications? We address each of these questions and more in detail below.

    Before we begin, we make one request of you: approach this topic with an open mind. It is easy to come in with pre-conceived notions of what machine intelligence is or can be. Depending on your background, such notions may or may not be well-founded. This topic might seem like science fiction, but below we will attempt to demonstrate that much of the hype surrounding machine intelligence, both optimistic and pessimistic, is grounded in reality.
    '''
    
    st.sidebar.header("Digging Deeper")
    st.sidebar.write("We are only grazing the surface with our main graphics, "
        + "but you can keep exploring! Below you will find options "
        + "for each section that will allow you to explore the data.")

# -----------------------------------------------------------------------------
# Chapter: History / Timeline
# -----------------------------------------------------------------------------

def render_history_chapter():
    """
    Render the history of machine intelligence chapter.
    """

    '''
    # A Brief History of Machine Intelligence

    Machine intelligence may seem like a distinctly modern phenomenon, but research into the subject has been going on for nearly seventy years. Some of major milestones related to the development of machine intelligence are highlighted in the timeline below.
    '''

    path = DATA_PATH + TIMELINE_DATA_FILENAME
    with open(path, "r") as f:
        data = f.read()

    # Render the timeline
    timeline(data, height=500)

# -----------------------------------------------------------------------------
# Chapter: Paradigm
# -----------------------------------------------------------------------------

def render_definition_section():
    """
    Render the definition section of the paradigm-shift chapter.
    """

    '''
    ### Definitions

    What do we mean when we refer to 'machine intelligence'?
    '''

def render_intelligence_section():
    """
    Render the 'importance of intelligence' section of the paradigm-shift chapter.
    """

    '''
    ### The Primacy of Intelligence

    Why is intelligence a matter of consequence?

    TODO: This section will contain an interactive visualization
    '''

def render_substrate_section():
    """
    Render the substrate distinction section of the paradigm-shift chapter.
    """

    '''
    ### The Potential of Mechanical Minds

    What are the implications of releasing intelligence from the bonds of a biological substrate?
    '''

def render_paradigm_chapter():
    """
    Render the paradigm shift chapter.
    """

    '''
    # Machine Intelligence: A Paradigm Shift

    Based on the milestones timeline above, its clear that machine intelligence has demonstrated its skill at defeating humans in the games we play. This may be demoralizing for top players, and makes for an interesting couple of days of news coverage, but is this really cause for concern or trepidation? In other words, one might be skeptical of the potential of machine intelligence on the basis of events that have been hailed a major milestones in its development history. Is it really that big of a deal?

    The answer is an unequivocal 'yes', but justification requires some additional explanation.
    '''

    render_definition_section()

    render_intelligence_section()

    render_substrate_section()

# -----------------------------------------------------------------------------
# Chapter: Perceptions
# -----------------------------------------------------------------------------

def render_perceptions_chapter():
    """
    Render chapter two.
    """

    '''
    ---
    # Perceptions versus Reality 

    TODO: Content here.
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
# Chapter: Prospects
# -----------------------------------------------------------------------------

odds_dict = {
    "1 in 2": 2, 
    "1 in 3" : 3, 
    "1 in 4" : 4, 
    "1 in 5" : 5, 
    "1 in 10" : 10
}

age_dict = {
    "18 to 29":"18 - 29",
    "30 to 44": "30 - 44", 
    "45 to 59": "45 - 59", 
    "60+" : "60"
}

gender_dict = {
    "Female": "female",
    "Male" : "male"
}

def user_selection(df):
    # Center the columns
    col1, col2, col3 = st.beta_columns([1,3,1])

    # Set up the radio buttons
    age_range = col2.radio("Choose your age bracket from the provided ranges.", ("-", "18 to 29", "30 to 44", "45 to 59", "60+"))   
    if age_range != "-":
        gender_at_birth = col2.radio("Choose your sex.", ("-", "Female", "Male"))
        if gender_at_birth != "-":
            odds = col2.radio(
                "Choose the Odds. Remember, this is the chance that humanity will face complete destruction.", 
                ("-", "1 in 2", "1 in 3", "1 in 4", "1 in 5", "1 in 10")) 
            if odds != "-":
                # Given the parameters get the specified percentages and graph for the user
                yes_or_no = col2.radio("Given the odds, should we as humanity continue to pursue this advancement?", ("-", "Yes", "No"))

                # Retrieve the specified row of data
                selection = df.loc[(df["Gender at Birth"] == gender_at_birth) & (df["Age Range"] == age_dict.get(age_range))
                            & (df["Odds"] == odds_dict.get(odds))]
                selection = selection.reset_index()
                graph_select = selection.melt(id_vars=["Age Range", "Gender at Birth"], value_vars=["No", "Yes"],
                                var_name = "Decision", value_name = "Percent")
                # Return specific message to user
                if yes_or_no != "-":
                    if yes_or_no == "Yes":
                        y_percent = ((selection.at[0, "Yes"])*100).round(1)
                        st.write("You agreed with " + str(y_percent) + " percent of individuals who are " + gender_dict.get(gender_at_birth) + 
                        " and are in the age bracket of " + age_range + " that we should press on despite the risks")
                    elif yes_or_no == "No":
                        n_percent = ((selection.at[0, "No"])*100).round(1)
                        st.write("You agreed with " + str(n_percent)  + " percent of individuals who are " + gender_dict.get(gender_at_birth) + 
                        " and are in the age bracket of " + age_range +  " that jeopardizing humanity to that degree is simply not worth it")
                    
                    # Build and return Bar chart
                    graph_title = "Decision Point: Odds " + odds
                    basic_bar = alt.Chart(graph_select).mark_bar().encode(
                            x=alt.X("Decision"),
                            y=alt.Y("Percent:Q", scale=alt.Scale(domain=(0, 1)), axis=alt.Axis(format="%", title="Percentage")),
                            color=alt.Color("Decision:N",scale=alt.Scale(scheme="redyellowblue")),
                            tooltip=[alt.Tooltip("Age Range:N"), alt.Tooltip("Gender at Birth:N"), alt.Tooltip("Percent:Q", format=".2%")]
                        ).properties(
                            title= graph_title
                        ).properties(
                            width=400,
                            height=350,
                        ).interactive()
                    
                    basic_bar = basic_bar.configure_title(
                        fontSize=30,
                        font="IBM Plex Sans")

                    col2.write(basic_bar)

                    st.write("Now feel free to explore more about the how the United States public responded to the survey using the sidebar.")

def regions_viz(oddsDf, odds):
    states = alt.topo_feature(vega_datasets.data.us_10m.url, 'states')
    subtitle = odds + " odds of total destruction of humanity - note percentages are by region"

    uschart = alt.Chart(states).mark_geoshape().encode(
            tooltip=["US Region:N", "State:N", alt.Tooltip("No:Q", format=".2%"), alt.Tooltip("Yes:Q", format=".2%")],
            color=alt.Color("Percentage That Said No:Q", scale=alt.Scale(scheme="redyellowblue", reverse=True))
        ).transform_lookup(
            lookup="id",
            from_=alt.LookupData(oddsDf, "id", ["US Region", "State", "No", "Yes", "Percentage That Said No"]),
        ).properties(
            width= DEFAULT_WIDTH,
            height= DEFAULT_HEIGHT,
        ).project(
            type="albersUsa"
        ).properties(
            title= {
            "text": ["Should we Continue to Pursue Advancement?"], 
            "subtitle": subtitle,
           }
        )

    uschart = uschart.configure_title(
        fontSize=30,
        font="IBM Plex Sans",
    )
    return uschart

def render_prospects_chapter():
    """
    Render chapter four user choice.
    """
    
    '''
    ---
    # Prospects for Machine Intelligence

    TODO: Content here.
    '''

    # Create centered title content
    # coll, colm = st.beta_columns([2,5.5])
    # colm.title('What Do You Choose?')
   
    '''
    
    In 2017 author Rick Webb wrote an article for NewCo Shift on machine superintelligence and public opinion. In the process of developing
    this article, he surveyed various populations in the United States. One of the questions posed was:
    
   "Humanity has discovered a scientific advancement. Pursuing it gives humanity two possible options: a chance that all of humanity 
    will die instantly, or a chance that poverty, death and disease will be cured for everyone, forever. Should we pursue it?"

    In his survey, Webb put the chance at varying levels to see how the public would respond, but the two results, transcendence or destruction, were always the same. 
    Now, we will give you a chance to do the same and see how you compare to the rest of the respondents.

    First select your age range and sex. This will let you see how you compare amongst others. Don't worry! You can use the sidebar
    later to explore further and compare across different ages and genders as well as look at how different regions across the United States
    differ in opinion. As a note, the survey only provided the option for male or female, so we unfortunately do not have data for other options at this time.

    Next, select one of the odds. The odds represent the chance that humanity will be destroyed. For example, 1 in 3 implies that one out
    of every three times, humanity will be completely and totally annihilated by the advancement we achieved. However, the other two times the
    result will be a world with no famine, disease, poverty, suffering, or death - in short a utopia. You decide whether we should continue down the path or not.
    '''
    
    # Set up the radio button theme
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.write('<style>div.row-widget.stRadio > div[role="radiogroup"] > label[data-baseweb="radio"] > div:first-child {background-color:'
        + COLOR_SCHEME_BLUE + '};</style>', unsafe_allow_html=True)
    st.markdown(
    """ <style>
            div[role="radiogroup"] >  :first-child{
                display: none !important;
            } 
        </style> """, unsafe_allow_html=True)

    # Let the use choose their fate
    selectDf = pd.read_csv(DATA_PATH + "grouped-Ending-Humanity.csv")
    user_selection(selectDf)

    # Sidebar
    st.sidebar.header("What Do You Choose?")
    st.sidebar.write(
        "Explore more about how the United States public responded to the survey. You can look at region maps as well as " 
        + "compare across different ages and genders.")
    
    region2 = pd.read_csv(DATA_PATH + "regions2-Ending-Humanity.csv")
    region3 = pd.read_csv(DATA_PATH + "regions3-Ending-Humanity.csv")
    region4 = pd.read_csv(DATA_PATH + "regions4-Ending-Humanity.csv")
    region5 = pd.read_csv(DATA_PATH + "regions5-Ending-Humanity.csv")
    region10 = pd.read_csv(DATA_PATH + "regions10-Ending-Humanity.csv")

    region_map_select = st.sidebar.selectbox(
        "Select on of the odds to see how different regions across the United States answered the survey question.",
        ("-", "1 in 2", "1 in 3", "1 in 4", "1 in 5", "1 in 10"))
    if region_map_select != "-":
        if region_map_select == "1 in 2":
            st.write(regions_viz(region2, region_map_select))
        elif region_map_select == "1 in 3":
            st.write(regions_viz(region3, region_map_select))
        elif region_map_select == "1 in 4":
            st.write(regions_viz(region4, region_map_select))
        elif region_map_select == "1 in 5":
            st.write(regions_viz(region5, region_map_select))
        else:
            st.write(regions_viz(region10, region_map_select))

# -----------------------------------------------------------------------------
# Chapter: Responses and Future Directions
# -----------------------------------------------------------------------------

def render_responses_chapter():
    """
    Render the responses chapter.
    """

    '''
    ---
    # Responses to Machine Intelligence
    
    TODO: Content here.
    '''

    '''
    ### What do the world powers think?
    '''

    # Read in data as csv
    COUNTRY_VOTES =  pd.read_csv("data/CountryVotesonAI.csv")
    
    # Combine totally agree/tend agree to one agree column for user clarity
    COUNTRY_VOTES["Agree"] = COUNTRY_VOTES["Tend_Agree"] + COUNTRY_VOTES["Totally_Agree"]
    
    # Combine totally disagree/tend disagree to one disagree column for user clarity
    COUNTRY_VOTES["Disagree"] = COUNTRY_VOTES["Tend_Disagree"] + COUNTRY_VOTES["Totally_Disagree"]
    COUNTRY_VOTES = COUNTRY_VOTES.rename(
        columns={
            "Totally_Agree": "Totally Agree",
            "Tend_Agree": "Tend Agree",
            "Tend_Disagree": "Tend Disagree",
            "Totally_Disagree": "Totally Disagree"
            })

    country_selector = alt.selection_multi(fields=["Country"], init=[{"Country":"Hungary"}])
    
    # Transform fold is conducted so that we can utilize the stacked bar approach
    # and analyze the huge discrepanacy between what world powers think
    
    '''
    ## World Power Believe on AI Safety and Regulation
    '''

    all_country_data = alt.Chart(COUNTRY_VOTES).mark_bar().encode(
        x=alt.X("Agree:Q", title="Percent Representatives that Want AI Regulation", scale=alt.Scale(domain=[0, 100])),
        y=alt.Y("Country:N", title="Country"), 
        color=alt.condition(country_selector, alt.value("#714141"), alt.value("#d9d9d9"))
    ).add_selection(
        country_selector
    ).interactive()


    by_country2 = alt.Chart(COUNTRY_VOTES).transform_fold(
        ["Agree", "Disagree"],
        as_=["Sentiment", "Agree/Disagree"]
    ).mark_bar().encode(
        x=alt.X("Country:N", title="Country"),
        y=alt.Y("Agree/Disagree:Q", title="Is AI Regulation Needed?", scale=alt.Scale(domain=[0, 100])),
        tooltip=[alt.Tooltip("Country:N", title="Country")], 
        color=alt.Color("Sentiment:N",
            scale = alt.Scale(domain=["Agree", "Disagree"], range=["#714141", "#d9d9de"])
        )
    ).transform_filter(
        country_selector
    ).interactive()

    joint_chart = all_country_data | by_country2
    st.write(joint_chart)

    '''
    From the chart above we can see that nearly every major world power agrees that AI imposes enough risk that it should be regulated. There is not one outlier nation that does not think that AI and Robotics are begning to play in increasingly dangerous or volatile role.
    '''

# -----------------------------------------------------------------------------
# Conclusion
# -----------------------------------------------------------------------------

def render_conclusion_content():
    """
    Render the conclusion content.
    """

    '''
    ---
    # Conclusion
    
    This concludes our discussion of machine intelligence.
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

    The datasets and prior work we referenced while working on this project are provided below.

    - Bostrom, Nick. [What Happens When Our Computers Get Smarter Than We Are?](https://www.youtube.com/watch?v=MnT1xgZgkpk&t=326s) TED Talk. 2015.
    - Harris, Sam. [Can We Build AI Without Losing Control Over It?](https://www.youtube.com/watch?v=8nt3edWLgIg) TED Talk. 2016.
    - McCarthy et al. _A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence._ 1955.
    - Muller, Vincent and Bostrom, Nick. Future Progress in Artificial Intelligence: A Survey of Expert Opinion. (2016).
    '''

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def main():

    # NOTE: Naturally, the order of the invocations here
    # defines the order in which our content is rendered
    # in the application. For sanity's sake, please ensure
    # that the order here matches the high-level order of
    # each of the chapters as they are defined above.

    render_introduction_content()

    render_history_chapter()

    render_paradigm_chapter()

    render_perceptions_chapter()
    
    render_prospects_chapter()

    render_responses_chapter()

    render_conclusion_content()

    render_references()

# -----------------------------------------------------------------------------
# Application Entry Point
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
