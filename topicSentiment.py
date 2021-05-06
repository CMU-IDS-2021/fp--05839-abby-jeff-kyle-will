import numpy as np
import pandas as pd
import altair as alt
import streamlit as st


def getTopByYear(data):
    df = {}
    cols = data.head()
    for col in cols:
        colName = str(col)
        df[colName] = data[col][0]
    return pd.DataFrame(df)

def getSentiment(data):
    newData = data.T
    cols = data.columns
    newData['Year'] = np.asarray(cols)
    newData.columns = ['Average Sentiment',' Positive Articles', 'Year']
    newData.set_index('Year')
    return newData.melt('Year', var_name='Legend', value_name='Percent')


def public():
    #Load data
    top10 = pd.read_json('data/top10_nature.json')
    sentiment = pd.read_json('data/natureArticlesSentiment.json')

    #Build Data
    topByYear = getTopByYear(top10)
    topByYear.index += 1
    sentByYear = getSentiment(sentiment)

    #Build slider
    top10s = {"2000" : "2000", "2001" : "2001",
              "2002" : "2002", "2003" : "2003",
              "2004" : "2004", "2005" : "2005",
              "2006" : "2006", "2007" : "2007",
              "2008" : "2008", "2009" : "2009",
              "2010" : "2010", "2011" : "2011",
              "2012" : "2012", "2013" : "2013",
              "2014" : "2014", "2015" : "2015",
              "2016" : "2016", "2017" : "2017",
              "2018" : "2018", "2019" : "2019",
              "2020" : "2020"}


    tops = st.select_slider("Select the year for the 'Top 10 Words' found in news articles", list(top10s.keys()))

    sentChart = alt.Chart(sentByYear).mark_line().encode(
        x=alt.X('Year:N'),
        y=alt.Y('Percent:Q', axis=alt.Axis(format='%')),
        color=alt.Color("Legend:N", legend=alt.Legend(orient='bottom'), scale=alt.Scale(scheme="redyellowblue"))
        ).properties(title="What is the perception of AI in the media?")
    line = alt.Chart(pd.DataFrame({' ': [tops]})).mark_rule(color="red").encode(x=' ')
    finalChart = sentChart + line
    col1, col2 = st.beta_columns([6,2])
    with col1:
        st.altair_chart(finalChart, use_container_width=True)
    with col2:
        st.dataframe(topByYear[tops])
    movies(tops)

def buildAcademicData(data):
    df = pd.DataFrame()
    topics = ["Language Models",
              "Cloud-Based ML Frameworks",
              "AI Based Multi-Lingual Translation",
              "Autonomous AI Decision Making",
              "Multi-Agent Pathfinding"]
    years = []
    topic1, topic2, topic3, topic4, topic5   = [], [], [], [], []
    for item in sorted(data.keys()):
        years.append(item)
        topic1.append(data[item][0])
        topic2.append(data[item][1])
        topic3.append(data[item][2])
        topic4.append(data[item][3])
        topic5.append(data[item][4])
    df[0] = topic1
    df[1] = topic2
    df[2] = topic3
    df[3] = topic4
    df[4] = topic5
    df = df.T
    df.columns = years
    df['Topics'] = topics
    return df

def academic():
    years = {"2013" : "2013",
              "2014" : "2014", "2015" : "2015",
              "2016" : "2016", "2017" : "2017",
              "2018" : "2018", "2019" : "2019",
              "2020" : "2020", "2021" : "2021"}
    data = pd.read_json("data/academicTopics.txt")
    acData = buildAcademicData(data)

    year = st.select_slider("Select the year to see the popular topics in AI research.", list(years.keys()))
    nData = acData[int(year)]
    source = pd.DataFrame({
        'Year' : nData.T,
        'Topics' : acData['Topics']
    })
    acChart = alt.Chart(source).mark_bar().encode(
        x=alt.X('Year:Q', scale=alt.Scale(domain=(0, 20))),
        y=alt.Y('Topics:N'),
        color=alt.Color("Topics:N", scale=alt.Scale(scheme='redyellowblue'))).properties(title="What topics are AI researchers focusing on?")
    st.altair_chart(acChart, use_container_width=True)

def movies(year):
    blurbs = {"2003":"The human city of Zion defends itself against the massive invasion of the machines as Neo fights to end the war at another front while also opposing the rogue Agent Smith.",
              "2004":"In 2035, a technophobic cop investigates a crime that may have been perpetrated by a robot, which leads to a larger threat to humanity.",
              "2014":"In 2028 Detroit, when Alex Murphy, a loving husband, father and good cop, is critically injured in the line of duty, the multinational conglomerate OmniCorp sees their chance for a part-man, part-robot police officer.",
              "2015":"In the near future, crime is patrolled by a mechanized police force. When one police droid, Chappie, is stolen and given new programming, he becomes the first robot with the ability to think and feel for himself.",
              "2016":"The rise of technology means that humans will have to be very clever not to be left behind as robots take over. But as human labor loses its value and challenges our purpose, people may find that they aren't wanted by the future at all.",
              "2017":"Young Blade Runner K's discovery of a long-buried secret leads him to track down former Blade Runner Rick Deckard, who's been missing for thirty years.",
              "2020":"Artificial Intelligence has permeated every aspect of planetary life in 2030. Tokyoites experience AI in every aspect of their lives whether medical, finance, transportation or their personal and day-to-day interactions. Many would tell you that AI is indispensable. Yet, as is often the case with technology jumping the gun on ethics and rules AI spins out of control and causes calamity after calamity. The city and the country are in chaos."}
    years = ["2003", "2004", "2014", "2015", "2016", "2017",]
    yearIndex = {"2003":"data/2003 - Matrix Reloaded.jpg",
                "2004":"data/2004 - i Robot.jpg",
                "2014":"data/2014 - RoboCop.jpg",
                "2015":"data/2015 - chappie.jpg",
                "2016":"data/2016 - Obsolete.jpg",
                "2017":"data/2017 -Blade_Runner_2049.png",
                "2020":"data/2020 - AI Amok.jpg"}
    narrative = {"2003":"In 2003, the movie The Matrix Reloaded debuted.  This is a story of a dystopian future where machines have taken over and supplanted humanity.  As you can see in the line chart, public perception shifted from positve to neutral and media articles were only 50% positive.  Did this movie affect the perception of AI?",
                 "2004":"In 2004, the blockbuster movie i, Robot premiered.  This story, while not wholely positive for AI, did have a robot protagonist that helped save the day with Will Smith. Did the perception of AI change again?",
                 "2014":"2014 was the year the robots turned on the populace.  In the movie, RoboCop, robots patrol the streets and have run amok, it is a cyborg that helped keep the streets safe.  Are movies and popular media influencing the public about AI?",
                 "2015":"Another shift in perception as the feelgood movie, Chappie, came out in theaters.  If a robot can feel, do we feel safer around them?",
                 "2016":"An indie film about how technology is supplanting humans.  Did the small scale of this movie mean that the perception only mildly drop?",
                 "2017":"Cult classic, BladeRunner, came out in the early 80's and was a movie about a dystopian future.  This sequel came out in 2017 and increased public perception.  Did the love of a continuation of a cult classic offset fear toward AI?",
                 "2020":""}
    col1, col2 = st.beta_columns([3,5])
    if year in years:
        with col1:
            st.image(yearIndex[year], width=300)
        with col2:
            st.subheader('Movie Description')
            st.write(blurbs[year])
            st.write()
            st.subheader('Was there an impact on perception?')
            st.write(narrative[year])
            
            
def flipProfData(data):
    topics = ["Language Models",
              "Cloud-Based ML Frameworks",
              "AI Based Multi-Lingual Translation",
              "Autonomous AI Decision Making",
              "Multi-Agent Pathfinding"]
    newData = data.drop("Topics", axis=1)
    newData = newData.T
    newData.columns = topics
    return newData

def topicTimeline(topic):
    unfixedData = pd.read_json("data/academicTopics.txt")
    data = buildAcademicData(unfixedData)
    data = flipProfData(data)
    nData = data[topic]
    years = ['2013','2014', '2015', '2016',
             '2017','2018', '2019', '2020', '2021']
    source = pd.DataFrame({
        'Years' : years,
        'Number of Articles' : nData.T
    })
    line = alt.Chart(source).mark_line(color='fcac64').encode(
        x= 'Years',
        y='Number of Articles:Q').properties(title="What topics are AI researchers focusing on?")

    st.write(f'Lets look at {topic} research over time.')
    st.altair_chart(line, use_container_width=True)
