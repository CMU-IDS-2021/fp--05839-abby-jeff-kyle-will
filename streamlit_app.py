  
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
COLOR_SCHEME_BLUE = "#bcdeea"
COLOR_SCHEME_ORANGE = "#ffbc79"

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

    TODO: This section will contain an interactive visualization regarding the shape of the spectrum of intelligence, and its importance in achieving those things we value. Most people are likely walk around with two implicit assumptions: 
    - The spectrum of intelligence is in some way _observable_; we think that we can make sense of the full spectrum of intelligence
    - Humans stand at or near the end of the spectrum of intelligence; we are the smartest things about which we have any knowledge

    The assumptions are very likely invalid. There is no reason to think that humans stand anywhere near the zenith of what is possible, nor is there reason to believe the intelligence curve does not extend far beyond what we might currently be able to observe.

    First, we need to establish the fact that intelligence is what distinguishes us from animals over which we (largely) dominate. For instance, apes are far stronger than humans pound-for-pound, yet the fate of the apes on Earth is almost entirely at the discretion of humanity, rather than in the hands of the apes themselves. QUESTION: How might we visualize this distinction?

    Second, we need to impress upon readers just how vast the spectrum of intelligence may actually be. This will likely take the form of a zoom-able plot similar to that in Sam Harris' TED talk (cited below) where we first show the relative distinction between "smart" people and "dumb" people, and then compare this distinction with what a machine intelligence might achieve relative to a "smart" person - the relationship is exponential.
    '''

def render_substrate_section():
    """
    Render the substrate distinction section of the paradigm-shift chapter.
    """

    '''
    ### The Potential of Mechanical Minds

    What are the implications of releasing intelligence from the bonds of a biological substrate? In this section we will compare Human Beings brain potential to the computerized counterparts. We will begin to see just how vastly computers outperform humans in the areas of brain frequency, speed, and storage capacity.

    '''
    
    '''
    - Frequency: Biological neruons fire at 20Hz. The clock speed in your run-of-the-mill laptop is 2GHz. This is a 10,000,000x difference, or seven orders of magnitude. Choose the brain type below (HUman, Computer) to see the vast difference between the combined freqneucy of 1000x human brains and that of a typical processor.
    '''
    from PIL import Image
    human_brain = Image.open('img/brain.png')
    brains = {
        "1000x Human": [20, "1000x Human Brain"],
        "Typical Processor": [700, "Typical Processor"],
    }
    brain = st.selectbox("Select your frequency.", list(brains.keys()))
    st.image(human_brain, caption=brains[brain][1], output_format='PNG', width=brains[brain][0])
    '''
    - Speed: Signals propagate in biological axons at ~150 m/s. The same signals propagate at the speed of light within an integrated circuit. In this domain, the computer vastly outperforms the human again.
    '''
    speedhuman = Image.open('img/speedhuman.png')
    speedairline = Image.open('img/speedairline.png')
    speedF35 = Image.open('img/speedF35.png')
    speedprocessor = Image.open('img/speedprocessor.png')
    speeds = {
        "Human": speedhuman,
        "Commericial Airline": speedairline,
        "F35 Fighter Jet": speedF35,
        "Typical Processor": speedprocessor,
    }
    speed = st.selectbox("Select your speed.", list(speeds.keys()))
    st.image(speeds[speed], output_format='PNG')
    '''
    - Capacity: The human cranium imposes tight size limitations on our brains. A mechanical mind that implements a machine intelligence has no such size restrictions. If we look at the typical human brain it can hold on average 2.5 million Gigabytes, whereas a small cloud facility holds about 400 million Gigbytes with all servers leveraged.
    '''
    storagehuman = Image.open('img/storagehuman.png')
    storagecomputer = Image.open('img/storagecomputer.png')
    storages = {
        "Human Storage": storagehuman,
        "Small Cloud Facility Storage": storagecomputer,
    }
    storage = st.selectbox("Select your storage capacity.", list(storages.keys()))
    st.image(storages[storage], output_format='PNG')
    
    

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

def render_popular_perceptions_section():
    """
    Render the popular perceptions section of the perceptions chapter.
    """

    '''
    ### Machine Intelligece in the Popular Media
     
    How do we characterize the popular public perception of machine intelligence?
    '''

    '''
    The following word cloud expresses some of the sentiment that can be seen in recent articles about machine intelligence.
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

    '''
    TODO: 
    - Scrape AI articles from google for 2010-2020
    - Create WordClouds for each year, switch charts based on slider or radio button
    - Run sentiment analysis and build overall yearly media sentiment analysis
      - Possibly break it down further into articles by year (10 articles per year)
    
    '''

def render_professional_perceptions_section():
    """
    Render the academic perceptions section of the perceptions chapter.
    """

    '''
    ### Machine Intelligence in Professional Settings

    How do we characterize the nature of research work on machine intelligence?
    '''

    '''
    TODO: Big idea for this section is a text analysis of academic work on machine intelligence. Specifically, the plan is to do the following:
    - Scrape PDF documents from the online Journal of Artificial Intelligence Research
    - Extract text from these PDF documents
    - Perform topic modeling on the documents (or just the titles? unclear if full text is feasible)
    - Visualize the distribution of documents over time according to the topic(s) in which they fall
    '''

def render_perceptions_chapter():
    """
    Render the perceptions chapter.
    """

    '''
    ---
    # Perceptions versus Reality 

    TODO: Content here.
    '''
    
    render_popular_perceptions_section()

    render_professional_perceptions_section()

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

si_impact = pd.DataFrame(np.array([[17,24,23,17,18], [28,25,12,12,24], [31,30,20,13,6], [20,40,19,13,8], [24,28,17,13,18]]),
                                  columns=['Extremely Good', 'Good', 'Neutral', 'Bad', 'Extremely Bad'], 
                                  index=['Participants of Conference on “Philosophy and Theory of AI”', 
                                         'Participants of the conferences of “Artificial General Intelligence”', 
                                         'Members of the Greek Association for Artificial Intelligence', 
                                         'The 100 ‘Top authors in artificial intelligence’', 'All Groups'])
def outlooks():
    colnames = list(si_impact.columns)
    si = si_impact.reset_index()
    si = si.rename(columns={'index': 'Group'})
    si = si.melt(id_vars=['Group'], value_vars=colnames,
            var_name='Outlook', value_name='Percent')
    si['Percent'] = si['Percent'].div(100)

    outlook_chart = alt.Chart(si).mark_bar().encode(
            x=alt.X('sum(Percent)',stack="normalize"),
            y=alt.Y('Group', title = None),
            color=alt.Color('Outlook:N',scale=alt.Scale(scheme="redyellowblue")),
            tooltip=[alt.Tooltip('Group:N'), alt.Tooltip('Outlook:N'), alt.Tooltip('Percent:Q', format='.1%')]
        ).properties(
            title='What Experts Expect from the creation of HLMI'
        ).configure_axis(
            labelLimit=1000
        ).properties(
            width=DEFAULT_WIDTH,
            height=400
        )

    outlook_chart = outlook_chart.configure_title(
        fontSize=20,
        font="IBM Plex Sans",
    )
    return outlook_chart


def render_expert_sentiment_section():
    """
    Render the expert sentiment section of the prospects chapter.
    """

    '''
    ### Expert Sentiment on Machine Intelligence

    TODO: This section will visualize some of the results of the 2016 survey of expert opinion on machine intelligence. This is an important section because it is one of the primary data points (aside from the professional analysis section above) that reveals just how high the degree of uncertainty is in the expert community.

    QUESTION(s):
    - The survey has a number of interesting questions, which ones do we want to visualize? All of them, accessible via dialog?
    - What is the most effective form factor for these charts?

    HLMI = Human Level Machine Intelligence
    '''
    slider_doom = st.slider("Guess the likelihood that if HLMI comes into existence that it will result in an existential catastrophe for the human race.",
                0.0, 100.0, 0.0)
    if slider_doom != 0.0:
        st.write("You guessed " + str(slider_doom) + "%. Across a variety of experts, the predicted likelihood is around 18%.")
        st.write(outlooks())

    #Sidebar
    st.sidebar.header("Expert Sentiment on Machine Intelligence")
    st.sidebar.write("Explore more responses from experts in the Machine Intelligence community.")



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

def prep_grouped_data(cdf):
    fullgrouptest = cdf.melt(id_vars=['Age Range', 'Gender at Birth', 'Odds'], value_vars=['No','Yes'], var_name = 'Decision', value_name = 'Percent')
    fullgrouptest['Combined'] = fullgrouptest.apply(lambda x: list([x['Gender at Birth'], x['Age Range'], x['Decision']]), axis=1)
    fullgrouptest['List'] = fullgrouptest['Combined'].apply(lambda x: ', '.join(map(str,x)))
    return fullgrouptest

def create_compare_chart(cdf, odds, ages, genders):
    df_odds = []
    df_ages = []
    for odd in odds:
        df_odds.append(odds_dict[odd])
    for age in ages:
        df_ages.append(age_dict[age])
    
    cdf = cdf[(cdf['Odds'].isin(df_odds))]
    cdf = cdf[(cdf['Gender at Birth'].isin(genders))]
    cdf = cdf[(cdf['Age Range'].isin(df_ages))]

    compare_chart = alt.Chart(cdf).mark_bar().encode(
            x=alt.X('List:O', title=None),
            y=alt.Y('Percent', scale=alt.Scale(domain=(0, 1)), axis=alt.Axis(format='%', title='Percentage')),
            color=alt.Color('Decision',scale=alt.Scale(scheme="redyellowblue")),
            column='Odds:N',
            tooltip=[alt.Tooltip('Gender at Birth'), alt.Tooltip('Age Range'), alt.Tooltip('Decision'), alt.Tooltip('Percent:Q', format='.2%')]
        ).properties(
            title='Comparing Decisions across different Ages, Genders, and Odds'
        ).configure_axis(
            labelLimit=1000
        )
    compare_chart = compare_chart.configure_title(
        fontSize=20,
        font="IBM Plex Sans",
    )
    return compare_chart 


def render_user_choice_section():
    """
    Render the user choice section of the prospects chapter.
    """
    
    '''
    ### What Would You Choose?

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
    #Color for MultiSelect
    st.write('<style>div[data-baseweb="select"] div {background-color:'
        + COLOR_SCHEME_BLUE + ';}</style>', unsafe_allow_html=True)
    
    # Let the use choose their fate
    selectDf = pd.read_csv(DATA_PATH + "grouped-Ending-Humanity.csv")
    user_selection(selectDf)

    # Sidebar
    st.sidebar.header("What Would You Choose?")
    st.sidebar.write(
        "Explore more about how the United States public responded to the survey. You can look at region maps as well as " 
        + "compare across different ages and genders.")
    
    #Region Visualization
    region2 = pd.read_csv(DATA_PATH + "regions2-Ending-Humanity.csv")
    region3 = pd.read_csv(DATA_PATH + "regions3-Ending-Humanity.csv")
    region4 = pd.read_csv(DATA_PATH + "regions4-Ending-Humanity.csv")
    region5 = pd.read_csv(DATA_PATH + "regions5-Ending-Humanity.csv")
    region10 = pd.read_csv(DATA_PATH + "regions10-Ending-Humanity.csv")

    region_map_select = st.sidebar.selectbox(
        "Select one of the odds to see how different regions across the United States answered the survey question.",
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

    #Comparing tool in the sidebar
    cdf = pd.read_csv(DATA_PATH + "grouped-Ending-Humanity.csv")
    cdf = prep_grouped_data(cdf)

    comparing_select_odd = st.sidebar.multiselect("Select one or more odds to compare across.",
                        ["1 in 2", "1 in 3", "1 in 4", "1 in 5", "1 in 10"])
    if comparing_select_odd != []:
        comparing_select_age = st.sidebar.multiselect("Select one or more age groups to compare across.",
                                ["18 to 29", "30 to 44", "45 to 59", "60+"])
        comparing_select_gender = st.sidebar.multiselect("Select one or both genders to compare across.",
                                ["Female", "Male"])

        if comparing_select_age != [] and comparing_select_gender != []:
            #once all options are present, produce the corresponding chart
            comparechart = create_compare_chart(cdf, comparing_select_odd, comparing_select_age, comparing_select_gender)
            st.write(comparechart)

def render_prospects_chapter():
    """
    Render chapter four user choice.
    """
    
    '''
    ---
    # Prospects for Machine Intelligence

    TODO: Content here.
    '''

    render_expert_sentiment_section()

    render_user_choice_section()

# -----------------------------------------------------------------------------
# Chapter: Responses and Future Directions
# -----------------------------------------------------------------------------

def render_world_powers_section():
    """
    Render the world powers section of the responses chapter.
    """
    
    '''
    ### Global Response

    What are the sentiments of the world powers regarding artificial intelligence regulation policy?
    '''

    # Read in data as csv
    COUNTRY_VOTES =  pd.read_csv("data/CountryVotesonAI.csv")

    # Combine totally agree/tend agree to one agree column for user clarity
    COUNTRY_VOTES["Agree"] = COUNTRY_VOTES["Tend_Agree"] + COUNTRY_VOTES["Totally_Agree"]

    # Combine totally disagree/tend disagree to one disagree column for user clarity
    COUNTRY_VOTES["Disagree"] = COUNTRY_VOTES["Tend_Disagree"] + COUNTRY_VOTES["Totally_Disagree"]

    # Rename columns for ease of reference
    COUNTRY_VOTES = COUNTRY_VOTES.rename(
        columns={
            "Totally_Agree": "Totally Agree",
            "Tend_Agree": "Tend Agree",
            "Tend_Disagree": "Tend Disagree",
            "Totally_Disagree": "Totally Disagree", 
            "Security_Incident": "Security Incident", 
            "Safe_Tech_Policies": "Safe Tech Training"
            })
    
    COUNTRY_VOTES["No Safe Tech Training"] = 100.0 - COUNTRY_VOTES["Safe Tech Training"]

    country_selector = alt.selection_multi(fields=["Country"], init=[{"Country":"Hungary"}])
    
    # Transform fold is conducted so that we can utilize the stacked bar approach
    # and analyze the huge discrepanacy between what world powers think
    
    '''
    ### National Stance on AI Safety and Regulation
    '''

# Transform fold is conducted so that we can utilize the stacked bar approach
# and analyze the huge discrepanacy between what world powers think
    all_country_data = alt.Chart(COUNTRY_VOTES).mark_bar().encode(
        tooltip=[alt.Tooltip("Country:N", title="Country")], 
        x=alt.X("Agree:Q", title="Percent Representatives that Want AI Regulation", scale=alt.Scale(domain=[0, 100])),
        y=alt.Y("Country:N", title="Country"), 
        color=alt.condition(country_selector, alt.value("#714141"), alt.value("#d9d9d9"))
    ).add_selection(
        country_selector
    ).interactive()


    by_country1 = alt.Chart(COUNTRY_VOTES).transform_fold(
        ["Security Incident"],
        as_=["% of Companies", "% Value"]
    ).mark_bar().encode(
        y=alt.Y("% Value:Q", title="% of Companies with Tech Security Incident", scale=alt.Scale(domain=[0, 100])),
        tooltip=[alt.Tooltip("Country:N", title="Country")], 
        color=alt.Color("% of Companies:N",
            scale = alt.Scale(domain=["Security Incident"], range=["#714141"])
        )
    ).transform_filter(
        country_selector
    ).interactive()

    by_country3 = alt.Chart(COUNTRY_VOTES).transform_fold(
        ["No Safe Tech Training"],
        as_=["% of Companies", "% Value"]
    ).mark_bar().encode(
        y=alt.Y("% Value:Q", title="% of Companies without Safe Tech Training", scale=alt.Scale(domain=[0, 100])),
        tooltip=[alt.Tooltip("Country:N", title="Country")], 
        color=alt.Color("% of Companies:N",
            scale = alt.Scale(domain=["No Safe Tech Training"], range=["#714141"])
        )
    ).transform_filter(
        country_selector
    ).interactive()

    joint_chart = all_country_data | by_country1 | by_country3
    st.write(joint_chart)

    '''
    From the chart above we can see that nearly every major world power agrees that AI imposes enough risk that it should be regulated. There is not one outlier nation that does not think that AI and Robotics are begning to play in increasingly dangerous or volatile role.
    '''

def render_responses_chapter():
    """
    Render the responses chapter.
    """

    '''
    ---
    # Responses to Machine Intelligence
    
    We have established the sentiments of both experts and members of the public regarding the future prospects of machine intelligence, but what is actually being done to address the inherent issues?
    '''

    render_world_powers_section()

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
    
    TODO: This conclusion needs to be much more compelling. This concludes our discussion of machine intelligence.
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
    - Webb, Rick. [Superintelligence and Public Opinion.](https://shift.newco.co/2017/04/24/superintelligence-and-public-opinion/) NewCo Shift. (2017).
    - Baobao Zhang & Allan Dafoe Artificial Intelligence, American Attitudes and Trends https://governanceai.github.io/US-Public-Opinion-Report-Jan-2019/addresults.html
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
