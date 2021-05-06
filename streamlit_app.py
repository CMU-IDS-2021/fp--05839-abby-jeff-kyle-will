  
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
import vega_datasets
import topicSentiment as ts
from PIL import Image


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
    Machine intelligence is a complex topic - technically, socially, politically, and ethically. Because of this complexity, navigating this topic requires a combination of both breadth and depth of understanding that is difficult to come by in most settings.

    In this application, we seek to provide you with the tools to navigate this topic effectively. What is machine intelligence, and why is it important? What is our current position, and how did we get here? What are the likely future implications, and what are we currently doing to shape this future? We address each of these questions and more in detail below.

    Before we begin, we make one request of you: approach this topic with an open mind. It is easy to come in with pre-conceived notions of what machine intelligence is, what it is not, and what it can be. Depending on your background, such notions may or may not be well-founded. This topic might seem like science fiction, but below we will attempt to demonstrate that much of the hype surrounding machine intelligence, both optimistic and pessimistic, is grounded in data and the best technical understanding we currently possess.
    '''
    
    st.sidebar.header("Digging Deeper")
    st.sidebar.write("We are only grazing the surface with our main graphics, "
        + "but you can keep exploring! Below you will find options "
        + "for each section that will allow you to explore the data.")

# -----------------------------------------------------------------------------
# Chapter: Definition / History
# -----------------------------------------------------------------------------

def render_definition_chapter():
    """
    Render the definition / history of machine intelligence chapter.
    """

    '''
    # Defining Machine Intelligence

    What do we mean by "machine intelligence"? The definition of the term has evolved somewhat with the technical capabilities in the field, but for the purposes of our exploration, we will simply use the term to mean *the realization of general intelligence capabilities in non-biological substrate*. There are two salient components of this definition:
    - We are concerned with _general_ intelligence; the other side of the spectrum, _narrow_ intelligence, poses its own set of risks and opportunities, but these are not our focus here
    - The substrate in which intelligence is achieved is immaterial; this implies that the term "machine" is used only loosely here, and that the form factor in which machine intelligence is realized might be far from what we might expect
    '''

    '''
    ### A Brief History
    Machine intelligence may seem like a distinctly modern phenomenon, but research into the subject has been going on for nearly seventy years. To get a better idea of what machine intelligence is and where it came from, we highlight some of the major milestones in the development of machine intelligence in the timeline below.
    '''

    path = DATA_PATH + TIMELINE_DATA_FILENAME
    with open(path, "r") as f:
        data = f.read()

    # Render the timeline
    timeline(data, height=500)

    '''
    ### Cars, Cats, and Playing Games

    After examining the events in the timeline above, one might be left with the impression that machine intelligence is little more than a novelty. We see that the technology is capable of helping us in our daily endeavors, perhaps by recognizing cat pictures and driving us where we need to go. While it does appear that machine intelligence has the capacity to surpass humans, it appears this phenomenon only occurs in narrow, game-playing settings that are hardly of interest to most. It is a long way from the chessboard to global domination; is machine intelligence truly a technology with vast disruptive potential?
    '''

# -----------------------------------------------------------------------------
# Chapter: Paradigm
# -----------------------------------------------------------------------------

def spect_intel(slide_val, df, pointsDf):
    points = alt.Chart(pointsDf).mark_circle(
            color="#ffbc79",
            size=300,
            clip=True
        ).encode(
            x=alt.X('x', title=None, axis=None, scale=alt.Scale(domain=(0, slide_val+0.1))),
            y=alt.Y('exp', title=None, axis=None, scale=alt.Scale(domain=(-2, 8105))),
        ).properties(
            width = DEFAULT_WIDTH,
            height = DEFAULT_HEIGHT
        )

    line = alt.Chart(df).mark_line(
                color="#bcdeea",
                size= 7,
                clip=True
            ).encode(
                x=alt.X('x', title=None, axis=None, scale=alt.Scale(domain=(0, slide_val+0.1))),
                y=alt.Y('exp', title=None, axis=None, scale=alt.Scale(domain=(-2, 8105))),
            ).properties(
                width = DEFAULT_WIDTH,
                height = DEFAULT_HEIGHT
            )

    text = points.mark_text(
                align='right',
                baseline='middle',
                dx=-10,
                dy= -15,
                font="IBM Plex Sans",
                fontSize = 15,
                fontWeight= 'bolder',
                clip=True,
                color="#ffbc79"
            ).encode(
                text='Type'
            )

    finalchart = line + points + text

    finalchart = finalchart.properties(
                title= {
                    "text": ["The Spectrum of Intelligence"], 
                    "subtitle": "Will Humans always be the Smartest Things Around?"

                }
            ).configure_title(
                    fontSize=40,
                    font="IBM Plex Sans",
            )
    return finalchart

def gen_exp():
    df = pd.DataFrame(np.random.randint(0, 11, size = 1000), columns=['x'])
    df['exp'] = np.exp(df['x'])
    pointsDf = pd.DataFrame([
        {'x': 1, 'Type': 'Chicken'},
        {'x': 5, 'Type': 'Average Human'},
        {'x': 6, 'Type': 'John von Neumann'},
        {'x': 9, 'Type': 'Machine Superintelligence'}
        ])
    pointsDf['exp'] = np.exp(pointsDf['x'])
    return df, pointsDf

def render_intelligence_section():
    """
    Render the 'importance of intelligence' section of the paradigm-shift chapter.
    """

    '''
    ### The Primacy of Intelligence

    **Intelligence Allows us to get What we Want** Why is intelligence a matter of consequence? An answer to this question requires that we recognize that intelligence is the foundational source of power and control in the world. Intelligence is what allows us to attain the things we value in this world. Consider for example the diction between humans and the many members of the animal kingdom over which we (largely) dominate. Apes are far stronger than humans, pound-for-pound. Tigers are faster and have much sharper teeth. Ants represent a far larger proportion of the Earth's overall biomass. Yet in each of these cases, the fate of the this animal on Earth is almost entirely at the discretion of humanity, rather than in the hands of the animal itself. The common factor in each comparison is human intelligence - the fact that we are the most intellectually-competent species around.
    
    **Human Intelligence is Nothing Special** So humans are the smartest species around, will this always be the case? There is no reason to think that this is so, or even that humans stand anywhere _near_ the zenith of what is possible. In fact, there is reason to believe that the intelligence curve extends far beyond what we might currently be able to observe and understand. What would be the implications for humanity if the spectrum of intelligence actually resembles something like the visualization below?
    '''

    df, pointsDf = gen_exp()
    slider_spect_intelligence = st.slider("Slide to Explore the Shape of the Intelligence Spectrum",
                0, 9, 0)
    st.write(spect_intel(slider_spect_intelligence, df, pointsDf))

    '''
    This visualization is not meant to actually quantify potential differences in level of intelligence, but merely highlight the fact that we (humans) might not even be able to conceive of the types of intelligence that are possible because of our own narrow viewpoint. However, is there any reason to believe that machine intelligence stands a chance of progressing to this point?
    '''


def magnitude_viz_speed(chart_type):
    speeds = pd.DataFrame([
            {'Speed': 300000000, 'Type': 'Computer Signals', 'row': 1},
            {'Speed': 18000, 'Type': 'F35 Fighter Jet', 'row': 2},
            {'Speed': 15000, 'Type': 'Commericial Airline', 'row': 3},
            {'Speed': 150, 'Type': 'Human Being Biological Axons', 'row': 4}
            ])

    speeds['Log Speed'] = np.log(speeds['Speed'])

    if chart_type == "Speed":
        speed_viz = alt.Chart(speeds).mark_bar().encode(
                x=alt.X('Speed:Q', title = "Speed (m/s)"),
                y=alt.Y('Type:O', title = None),
                color=alt.Color('Type:O',scale=alt.Scale(scheme="redyellowblue")),
                tooltip=[alt.Tooltip('Type:O'), alt.Tooltip('Speed:Q')]
        ).properties(
            width=30000,
            height=400,
        ).properties(title= {
                    "text": ["Comparing Speeds"], 
                    "subtitle": "When directly comparing various objects, it is difficult to visually see the difference between the slower objects",
                }
        )
    else:
        speed_viz = alt.Chart(speeds).mark_bar().encode(
                x=alt.X('Log Speed:Q', title = "Logarithmic Values of Various Speed (m/s)"),
                y=alt.Y('Type:O', title = None),
                color=alt.Color('Type:O',scale=alt.Scale(scheme="redyellowblue")),
                tooltip=[alt.Tooltip('Type:O'), alt.Tooltip('Speed:Q'), alt.Tooltip('Log Speed:Q')]
        ).properties(
            width=10000,
            height=400,
        ).properties(title= {
                    "text": ["Comparing Logarithmic Speeds"], 
                    "subtitle": "In order to actually visually difference between some of the slower objects, we must convert via logarithm",
                }
        )
    
    speed_viz = speed_viz.configure_title(
        fontSize=30,
        font="IBM Plex Sans",
        anchor='start'
    )

    return speed_viz


def magnitude_viz_brain():
    source = pd.DataFrame([
                {'count': 1, 'Type': 'computer processor', 'row': 1},
                {'count': 1000, 'Type': '1000 human beings', 'row': 2},
                {'count': 1000, 'Type': '1000 human beings', 'row': 3},
                {'count': 1000, 'Type': '1000 human beings', 'row': 4},
                {'count': 1000, 'Type': '1000 human beings', 'row': 5},
                {'count': 1000, 'Type': '1000 human beings', 'row': 6},
                {'count': 1000, 'Type': '1000 human beings', 'row': 7},
                {'count': 1000, 'Type': '1000 human beings', 'row': 8},
                {'count': 1000, 'Type': '1000 human beings', 'row': 9},
                {'count': 1000, 'Type': '1000 human beings', 'row': 10},
                {'count': 1000, 'Type': '1000 human beings', 'row': 11}
                ])

    source['emoji'] = [{'1000 human beings': '🛉', 'computer processor': '💻'}[t]*int(cnt) for t,cnt in source[['Type', 'count']].values]
    source.head()

    mag_viz = alt.Chart(source).mark_text(size=30, align='left').encode(
            alt.X('count:O', axis=None, scale=alt.Scale(range=[0,100])),
            alt.Y('row:O', axis = None),
            alt.Text('emoji:N')
        ).properties(width=20000, height=400
        ).transform_calculate(
            value='0'
        ).properties(title="Another Look at the Frequency Magnitude", 
        ).properties(background='#f2f2f2')


    mag_viz = mag_viz.configure_title(
        fontSize=35,
        font="IBM Plex Sans",
        anchor='start',
        color='black'
    )

    return mag_viz


def render_substrate_section():
    """
    Render the substrate distinction section of the paradigm-shift chapter.
    """

    '''
    ### The Potential of Mechanical Minds

    What are the implications of releasing intelligence from the bonds of a biological substrate? In this section we will compare Human Beings brain potential to the computerized counterparts. We will begin to see just how vastly computers outperform humans in the areas of brain frequency, speed, and storage capacity.

    '''

    st.sidebar.header("The Potential of Mechanical Minds")
    st.sidebar.write("Select other options to understand the scale of the differences between a Human Being and a Computer")
    scale_opt = st.sidebar.selectbox("Select an option", ("Frequency", "Speed", "Storage"))

    if scale_opt == "Frequency":
        alt_brain = st.sidebar.radio("Look at an alternative magnitude visualization", ("-", "Alternative Magnitude"))
        '''
        - Frequency: Biological neruons fire at 20Hz. The clock speed in your run-of-the-mill laptop is 2GHz. This is a 10,000,000x difference, or seven orders of magnitude. Choose the brain type below (Human, Computer) to see the vast difference between the combined freqneucy of 1000x human brains and that of a typical processor.
        '''
        human_brain = Image.open('img/brain.png')
        brains = {
            "100,000x Human": [10, "100,000x Human Brain"],
            "500,000x Human": [50, "500,000x Human Brain"],
            "1,000,000x  Human": [100, "1,000,000x Human Brain"],
            "2,500,000x  Human": [250, "2,500,000x Human Brain"],
            "5,000,000x Human": [500, "5,000,000x Human Brain"],
            "7,500,000x Human": [750, "7,500,000x Human Brain"],
            "Typical Processor": [1000, "Typical Processor"]
        }
        brain = st.select_slider("Select your frequency.", list(brains.keys()))
        st.image(human_brain, caption=brains[brain][1], output_format='PNG', width=brains[brain][0])
        '''
        '''
        if alt_brain == "Alternative Magnitude":
            st.write("Each human icon is equivalent to the combined frequency of 1000 human beings. Scroll to see the full impact.")
            st.write(magnitude_viz_brain())
        
    elif scale_opt == "Speed":
        alt_speed = st.sidebar.radio("Look at alternative magnitude visualizations", ("-", "Speed", "Logarithim of Speed"))
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
        speed = st.select_slider("Select your speed.", list(speeds.keys()))
        st.image(speeds[speed], output_format='PNG')

        if alt_speed == "Speed":
            st.write(magnitude_viz_speed(alt_speed))
        elif alt_speed == "Logarithim of Speed":
            st.write(magnitude_viz_speed(alt_speed))

    else:
        '''
        - Capacity: The human cranium imposes tight size limitations on our brains. A mechanical mind that implements a machine intelligence has no such size restrictions. If we look at the typical human brain it can hold on average 2.5 million Gigabytes, whereas a small cloud facility holds about 400 million Gigbytes with all servers leveraged.
        '''
        storagehuman = Image.open('img/HumanStorage.png')
        storage4 = Image.open('img/4ServerStorage.png')
        storage9 = Image.open('img/9ServerStorage.png')
        storage16 = Image.open('img/16ServerStorage.png')
        storage25 = Image.open('img/25ServerStorage.png')
        storage81 = Image.open('img/81ServerStorage.png')
        storage156 = Image.open('img/156ServerStorage.png')
        storages = {
            "Human": storagehuman,
            "4x 2U Server Rack": storage4,
            "9x 2U Server Rack": storage9,
            "16x 2U Server Rack": storage16,
            "25x 2U Server Rack": storage25,
            "81x 2U Server Rack": storage81,
            "Small Cloud Facility": storage156,
        }
        storage = st.select_slider("Select your storage capacity.", list(storages.keys()))
        st.image(storages[storage], output_format='PNG')
    
    

def render_paradigm_chapter():
    """
    Render the paradigm shift chapter.
    """

    '''
    # A Paradigm Shift

    Based on the milestones timeline above, its clear that machine intelligence has demonstrated its prowess in select areas of human endeavor. This may be demoralizing for the world's Chess and Go players, and makes for an interesting couple of days of news coverage, but is this really cause for concern or trepidation? In other words, one might be skeptical of the potential of machine intelligence on the basis of events that have been hailed a major milestones in its development history. Is it really that big of a deal?

    The answer is an unequivocal 'yes', but justification requires some additional explanation.
    '''

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
    With the prevalence of research and popular movies about Artificial Intelligence, it would be safe to say that the public has some thoughts and opinions on Artificial Intelligence.
    
    Did you know that there were 182 movies that featured Artificial Intelligence in some form from 2000-2020?  With provocative titles such as "AI Amok" (2020) and "RoboCop" (2014), was public perception of AI affected by these movies?  Let's Explore the perception of machine intelligence in the media..
    
    We pulled all news articles from Nature.com from 2000-2020 that featured Artificial Intelligence.  These articles do not include any journal or academic publications.  We then performed a sentiment analysis on the content in the articles to judge the overarching sentiment of the reporting and tallied the number of positve articles vs negative articles.
    
    As you can see below the percentage of articles that are positive is almost consistently 100%.  Even when looking at the overall perception, you can see that it is actually pretty close to neutral in all years. There are a few explanations that could answer the question, but lets see if there is a correlation between hit-movies and the perception in news media.  
    
    Were there popular movies that may have affected the public perception of Artificial Intelligence and caused the sentiment analysis of these articles to trend toward neutral from the positvive.  Slide the bar to the right and see.
    
    ### Sentiment and Perception in the Public Media
    '''
    ts.public()

    '''
    Many of the media articles are slightly above neutral. This can be intepreted a few ways in that we can infer that humanity is wary of AI and machine intelligence or that we are playing a wait and see game.  It could be a combination of both.   Can we really say that the future of machine intelligence or Artificial Intelligence is bleak?  Should we be afraid?  Let's explore what is being researched in the field of AI.
    '''

def render_professional_perceptions_section():
    """
    Render professional perceptions
    """
    '''
    
    ### Machine Intelligence in Professional Settings

    How do we characterize the nature of research work on machine intelligence?
    
    Research in the field of Artificial Intelligence is growing quickly. Over the last 8 years, there have been over 500 publications regarding Artificial Intelligence and related topics from a single journal source: the Journal of Artificial Intelligence Research.  
    
    We looked at the title of each article and built a topic model to gather the most popular 5 topics.  Using this model, we discovered that almost 20% of the articles published on these fields of research. 
    
    The first chart shows us how many articles are being published in a given year that are on the most popular topics.  AI Based Multi-Lingual translation is a field that is expanding quickly and some avenues of research are developing on the fly audio translation from multiple languages.  
    
    Autonomous AI Decision Making is the prodcess of making decision without human oversight.  Some focus areas are healthcare, where, according to Science Direct, "clinical decisions are made without human oversight."  
    
    Cloud-Based ML Frameworks is an area of research that seeks to create robust and modular cloud based systems to do machine learning.  
    
    Language Models is another aspect of research that is focused on predicting words.  This may sound simple, but languages have many rules and grammatical foibles that make this difficult. 
    
    The last popular topic is Multi-agent pathfinding.  This area of research is based on calculating the best path for multiple objects in realt time.  Imagine a machine intelligence trying to calculate the most optimal route for every care on the road. 
    
    As you can see in the chart below, there are a number of research papers that are on one of the top-5 topics.  As you move the slider over you can see how things change over time.  For a different perspective, you can track a single topic from the sidebar and follow the research pattern over time.
    '''
    ts.academic()
    topics = ["Language Models",
              "Cloud-Based ML Frameworks",
              "AI Based Multi-Lingual Translation",
              "Autonomous AI Decision Making",
              "Multi-Agent Pathfinding"]


    st.sidebar.header("Tracking Academic Research")
    st.sidebar.write("Select each option to observe the shift in research priorities.")
    pTopic = st.sidebar.selectbox("Select an option", topics)
    ts.topicTimeline(pTopic)
    '''
    The AI Based Multi-Lingual topic seems to be trending upward from 2020 into 2021.  That is an interesting observation that could be related to the COVID-19 pandemic.  As many people are teleworking, is there a greater call for instant translation of multiple languages?  Is this a boon to humanity as we strive to counter the virus that is destroying our world?
    
    Autonomous AI Decision Making is also trending up in 2021.  The optimistic view of this is that AI will help derive vaccine genomes to help with stopping the virus, the pessimistic view is that the AI will start making decisions that could negatively impact us.  Who knows what the future holds?
    '''

def render_perceptions_chapter():
    """
    Render the perceptions chapter.
    """

    '''
    ---
    # Perceptions versus Reality
    
    How much do we really know about machine intelligence or Artificial Intelligence? What are the perceptions of AI that guide humanity toward the future?  Are we thinking positiviely? Negatively? Are we neutral?
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

def dev_hmli():
    progess = pd.DataFrame(np.array([47.9, 42.0, 42.0, 39.6, 37.3, 35.5, 34.9, 32.5,29.0, 29.0, 23.7, 21.3, 20.7, 17.8, 13.6, 4.1, 2.6]), 
                                columns=['Percent'],
                               index=['Cognitive Science', 'Integrated Cognitive Architectures', 'Algorithms Revealed by Computational Neuroscience',
                                      'Artificial Neural Networks', 'Faster Computing Hardware', 'Large-scale Datasets', 'Embodied systems',
                                      'Other method(s) currently completely unknown', 'Whole Brain Emulation', 'Evolutionary Algorithms or Systems',
                                      'Other method(s) currently known to at least one investigator', 'Logic-based Systems', 
                                      'Algorithmic Complexity Theory', 'No method will ever contribute to this aim', 'Swarm Intelligence',
                                      'Robotics', 'Bayesian Nets'])
    progess = progess.reset_index()


    devhmli = alt.Chart(progess).mark_bar().encode(
            x=alt.X('index:O', title = None),
            y=alt.Y('Percent:Q', title = 'Percent Likelihood that the Topic Will Impact the Development of HLMI'),
            color=alt.Color('index:O',scale=alt.Scale(scheme="redyellowblue")),
            tooltip=[alt.Tooltip('index:O'), alt.Tooltip('Percent:Q')]
        ).properties(
            width=DEFAULT_WIDTH,
            height=DEFAULT_HEIGHT,
        ).properties(
            title= "What Will Impact the Development of HLMI"
        ).configure_axis(
            labelLimit=1000
        ).configure_title(
            fontSize=20,
            font="IBM Plex Sans",
        ).interactive()
    return devhmli

def render_expert_sentiment_section():
    """
    Render the expert sentiment section of the prospects chapter.
    """

    '''
    ### Expert Sentiment on Machine Intelligence

    The conjecture that **every aspect of learning** can be simulated by a machine if it is describe precisely enough forms the base of
    the pursuit of artificial intelligence. This concept helps define how current research in AI approaches continued development in the field.
    But, what does achieving true AI and beyond that super intelligence actually mean? And how soon can we expect to see it?

    This became the premise for a series of surveys and questionaries created by Vincent Muller and Nick Bostrom and directed at subject
    matter experts in artificial and machine intelligence. These questions were not only attempting to gauge the likelihood of achieveing
    high level machine intelligence (HLMI), but also to assess the outcome of such an achievement if it was to occur.

    Here we highlight some of the key results from the 2016 survey. 

    '''
    slider_doom = st.slider("Guess the likelihood that if HLMI comes into existence that it will result in an existential catastrophe for the human race.",
                0.0, 100.0, 0.0)
    if slider_doom != 0.0:
        st.write("You guessed " + str(slider_doom) + "%. Across a variety of experts, the predicted likelihood of high level machine intelligence resulting in existential catastrophe is around 18%.")
        st.write(outlooks())
        '''
        Whether the experts placed their predictions higher or lower than yours, the larger takeaway is this: **the probability is non-zero**. In fact,
        it is roughly one in five. The debate about whether we will ever reach HLMI is unresolved among experts. Some
        believe HLMI and other critical aspects that would be required to achieve HLMI will never exist. Others feel we could see these
        achievements within a few decades. You can explore more with the sidebar. 

        One piece is absolutely clear. **We have no idea what the consequences of high level machine intelligence will be**.
        '''

    #Sidebar
    st.sidebar.header("Expert Sentiment on Machine Intelligence")
    st.sidebar.write("Explore more responses from experts in the Machine Intelligence community.")
    hlmi = st.sidebar.selectbox("Select an option to view more visualizations based on expert opinions.", 
        ("-", "What Will Impact the Development of HLMI", "Simulate Learning", "Basic Operations", "Brain Architecture"))

    if hlmi == "What Will Impact the Development of HLMI":
        '''
        '''
        '''
        Advancements in every field are made daily, but only some will be able to directly contribute to our development of high level machine 
        intelligence. Below are a variety of fields that experts feel could directly contribute to the body of knowledge required to achieve
        HLMI. Note percenatges are not normalized.
        '''
        st.write(dev_hmli())
    elif hlmi == "Simulate Learning":
        names = ['Today','Within 10 years', 'Between 11 and 25 years', 'Between 26 and 50 years', 'More than 50 years', 'Never']
        size = [0,5,2,11,41,41]
        percents = ['Today: 0%', 'Within 10 years: 5%','Between 11 and 25 years: 2%','Between 26 and 50 years: 11%',
                    'More than 50 years: 41%', 'Never: 41%']
        
        fig= plt.figure()

        # Create a circle at the center of the plot
        my_circle = plt.Circle( (0,0), 0.7, color='white')

        # Give color names
        wedges, texts = plt.pie(size, labels=percents, colors=['#e75a3b','#fa9e5d','#faf8c1','#d7eeec','#81b5d5','#3f58a6'])
        p = plt.gcf()
        p.gca().add_artist(my_circle)

        plt.legend(wedges, names,
                title="How Soon Will We Achieve This",
                loc="center left",
                bbox_to_anchor=(1.2, -0.3, 0.5, 1))

        # Show the graph
        st.header("The Earliest Machines Will be Able to Simulate Learning and Every Other Aspect of Human Intelligence")
        st.pyplot(fig)
        '''
        While no one believes we can currently simulate true human-like learning, more than half of the experts believe it is achieveable.
        This is a foundational building block for achieving HLMI, and how a machine could rapidly outpace the abilities of any human. 
        '''
    
    elif hlmi == "Basic Operations":
        names = ['Today','Within 10 years', 'Between 11 and 25 years', 'Between 26 and 50 years', 'More than 50 years', 'Never']
        size = [6,12,10,21,29,21]
        percents = ['Today: 6%', 'Within 10 years: 12%','Between 11 and 25 years: 10%','Between 26 and 50 years: 21%',
                    'More than 50 years: 29%', 'Never: 21%']
        
        fig = plt.figure()

        # Create a circle at the center of the plot
        my_circle = plt.Circle( (0,0), 0.7, color='white')

        # Give color names
        wedges, texts = plt.pie(size, labels=percents, colors=['#e75a3b','#fa9e5d','#faf8c1','#d7eeec','#81b5d5','#3f58a6'])
        p = plt.gcf()
        p.gca().add_artist(my_circle)

        plt.legend(wedges, names,
                title="How Soon Will We Achieve This",
                loc="center left",
                bbox_to_anchor=(1.2, -0.3, 0.5, 1))

        # Show the graph
        st.header("The Earliest We Will Understand the Basic Operations of the Human Brain Sufficiently to Create Machine Simulation of Human Thought")
        st.pyplot(fig)
        '''
        The basic operations of the brain, though still immensely complex, are likely the most feasible to achieve. Some experts believe
        we already have a sufficient enough understanding to percisely describe and thus replicate these operations today. This achievement is
        the first major step towards HLMI.  
        '''

    elif hlmi == 'Brain Architecture':
        names = ['Today','Within 10 years', 'Between 11 and 25 years', 'Between 26 and 50 years', 'More than 50 years', 'Never']
        size = [0,11,14,22,40,14]
        percents = ['Today: 0%', 'Within 10 years: 11%','Between 11 and 25 years: 14%','Between 26 and 50 years: 22%',
                    'More than 50 years: 40%', 'Never: 14%']
        
        fig = plt.figure()

        # Create a circle at the center of the plot
        my_circle = plt.Circle( (0,0), 0.7, color='white')

        # Give color names
        wedges, texts = plt.pie(size, labels=percents, colors=['#e75a3b','#fa9e5d','#faf8c1','#d7eeec','#81b5d5','#3f58a6'])
        p = plt.gcf()
        p.gca().add_artist(my_circle)

        plt.legend(wedges, names,
                title="How Soon Will We Achieve This",
                loc="center left",
                bbox_to_anchor=(1.2, -0.3, 0.5, 1))

        # Show the graph
        st.header("The Earliest We Will Understand the Architecture and Structure of the Brain Sufficiently to Create Machine Simulation of Human Thought")
        st.pyplot(fig)
        '''
        The architecture of the brain, still eludes our full understanding though most experts believe we will reach a point of full 
        understanding in the next few decades. This would provide us insight into how the organizational control of our brain is structured,
        and will likely be key in developing machine intelligence beyond the capacity of our own in all regards, not just in a few areas. 
        '''


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
                        " and are in the age bracket of " + age_range + " that we should press on despite the risks.")
                    elif yes_or_no == "No":
                        n_percent = ((selection.at[0, "No"])*100).round(1)
                        st.write("You agreed with " + str(n_percent)  + " percent of individuals who are " + gender_dict.get(gender_at_birth) + 
                        " and are in the age bracket of " + age_range +  " that jeopardizing humanity to that degree is simply not worth it.")
                    
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

                    '''
                    Even in the most extreme cases, many feel a case can be made to keep exploring. Existential risks, and by extention the true extinction of 
                    the human race, is difficult to fathom. Moreover, human beings are notoriously bad a conceptually understanding odds. It is possible
                     with a rewording or restructuring of the question, the outcome may be different. But, as long as a non-trivial portion of society 
                     continues to support unburdened progress with disregard for the risks, humankind will remain **at the mercy of the unintended consequences - good or bad**. 
                     Now feel free to explore more about the how the United States public responded to the survey using the sidebar.")
                    '''

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
        '''
        '''
        '''
        Below is a map of the United States broken into regions to better observe how the distribution of beliefs about the path
        humanity should take changes as one traverses the country. It is intereseting to see distinct differences in the regions that
        are in some cases fairly extreme. Various factors play a role in why these differences exist from ethnic backgrounds to religion. 
        Colors indicate the proportion of the population in each region that believe we should **not** pursue advancement and jeopardize the human race.
        '''
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
            '''
            '''
            '''
            The graphs here provide further exploration to the bar graph seen after you made your decision about pursuing advancement.
            Now you can investigate how age, gender, and the odds themselves influence how individuals make their decisions.
            '''
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
    ### Global Response and Status

    What are the sentiments of the world powers, specifically the EU Countries regarding artificial intelligence regulation policy? Furthermore, what are they doing about it?
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

    all_country_data = alt.Chart(COUNTRY_VOTES).mark_bar().encode(
        tooltip=[alt.Tooltip("Country:N", title="Country")], 
        x=alt.X("Agree:Q", title="Percent Representatives that Want AI Regulation", scale=alt.Scale(domain=[0, 100])),
        y=alt.Y("Country:N", title="Country"), 
        color=alt.condition(country_selector, alt.value("#ffbc79"), alt.value("#d9d9d9"))
    ).add_selection(
        country_selector
    ).interactive()


    by_country1 = alt.Chart(COUNTRY_VOTES).transform_fold(
        ["Security Incident"],
        as_=["Digital Safety Metric", "% Value"]
    ).mark_bar().encode(
        y=alt.Y("% Value:Q", title="% of Companies with Tech Security Incident", scale=alt.Scale(domain=[0, 100])),
        tooltip=[alt.Tooltip("Country:N", title="Country")], 
        color=alt.Color("Digital Safety Metric:N",
            scale = alt.Scale(domain=["Security Incident"], range=["#bcdeea"])
        )
    ).transform_filter(
        country_selector
    ).interactive()

    by_country3 = alt.Chart(COUNTRY_VOTES).transform_fold(
        ["No Safe Tech Training"],
        as_=["Digital Safety Metric", "% Value"]
    ).mark_bar().encode(
        y=alt.Y("% Value:Q", title="% of Companies without Safe Tech Training", scale=alt.Scale(domain=[0, 100])),
        tooltip=[alt.Tooltip("Country:N", title="Country")], 
        color=alt.Color("Digital Safety Metric:N",
            scale = alt.Scale(domain=["No Safe Tech Training"], range=["#bcdeea"])
        )
    ).transform_filter(
        country_selector
    ).interactive()

    joint_chart = all_country_data | by_country1 | by_country3
    st.write(joint_chart)

    '''
    From the chart above we can see that nearly every major EU power agrees that AI imposes enough risk that it should be regulated. There is not one outlier nation that does not think that AI and Robotics are begning to play in increasingly dangerous or volatile role. However, when we inspect each country we can see that each country has had a non-trivial amount of cyber security incidents. Additionally, a large handful of corporations in each country do not have any kind of digital saftey training at work whatsoever. Does this not foreshadow the next catastrophic event? AI is increasing at a rapid rate, yet safety does not seem to be a major concern. Select the US Case Study option on the sidebar to the left to view first hand how lack of regulation is letting AI get out of hand.
    '''

    st.sidebar.header("Global Respons and Status")
    case_study_select = st.sidebar.radio("Select the case study to learn more.", ("-", "US Case Study"))
    if case_study_select == "US Case Study":
        '''
        ### US Case Study: Self-Driving Cars and their Lack of Regulation
        Now that we've taken a look at what our counterparts in the EU believe, let's take a look back at America and a specific policy-case, "Self-Driving Cars". Traditionally, the regulation governing what cars are allowed to make it out onto the roadways is the FMVSS or Federal Motor Vehicle Safety Standards. These laws cover a wide array of aspects. However, they cover nothing to do with self-driving cars such as cyber-attacks, proper testing, software updates, emergency scenarios, etc. In September 2017, the House of Representatives did propose additional requirements to the FMVSS for autonomous cars, however, this proposal did not make it past the Senate. A Presidential Administration largely focused on minimal regulation certainly did not help the issue.
        '''
        '''
        But who would possibly want less regulation on such a dangerous endeavor? 
        '''
        '''
        The answer is businesses and the locations that want to attract them. Two of the hotbeds for self-driving car research are Arizona and our own state Pennsylvania. Contrary to popular belief, the location in Pittsburgh is not solely due to NREC or CMU, but rather Pennsylvania's loose regulations on self-driving car testing. 
        '''
        '''
        You may be surprised to find that several incidents have occurred right here in Pittsburgh including an event in 2018 when a self-driving car slammed into an unsuspecting driver. The incidents get much more grave. Looking to make self-driving cars cheaper, Uber disabled what is called a LIDAR system in one of their Arizona vehicles. Without the costly system the car hit and killed a pedestrian. 
        '''
        '''
        So when is enough? Clearly, these businesses only have testing, training, and profits in mind. Perhaps, the local governments do too. Regulation is needed on a larger scale, however, it is largely non-existent. 
        '''
        crash = Image.open('img/Ubercrash.jpg')
        st.image(crash)

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
    
    This concludes our exploration of machine intelligence. In the narrative above, we saw some of major milestones in the technology's development, along with some accompanying evidence that suggests the disruptive potential it has. Next, we compared coverage of machine intelligence research in popular media with its treatment in academic settings. We then explored the sentiments regarding the long-term prospects of machine intelligence from both expert and non-expert sources. Finally, we examined the current state of the response to advances in machine intelligence in the form of national-level policies.
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
    - Timothy Lee B, Self-Driving Car Article, 2018 https://arstechnica.com/cars/2018/04/the-way-we-regulate-self-driving-cars-is-broken-heres-how-to-fix-it/
    - Brain png image, https://www.cleanpng.com/png-drawing-cartoon-character-human-brain-7352936/
    - Box png image, https://toppng.com/free-image/cardboard-box-PNG-free-PNG-Images_30993
    - Spedomoter png image, https://www.pngkey.com/pngs/speedometer/
    - Paul Reber, Human Brain Storage, 2010, https://www.scientificamerican.com/article/what-is-the-memory-capacity/
    - EU Data Eurostat, 2021, https://ec.europa.eu/eurostat/web/main/data/database
    - Richard Waters, Uber crash, 2017, https://www.ft.com/content/89692fee-1181-11e7-80f4-13e067d5072c
    - Nature, https://www.nature.com
    - Journal of Artificial Intelligence Research, https://www.jair.org/
    - Internet Movie Database (IMDb), https://www.imdb.com/
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

    render_definition_chapter()

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
