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
        color=alt.Color("Legend:N", legend=alt.Legend(orient='bottom'))
        ).properties(title="What is the perception of AI in the media?")
    line = alt.Chart(pd.DataFrame({' ': [tops]})).mark_rule(color="red").encode(x=' ')
    finalChart = sentChart + line
    col1, col2 = st.beta_columns([6,2])
    with col1:
        st.altair_chart(finalChart, use_container_width=True)
    with col2:
        st.dataframe(topByYear[tops])

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
        y=alt.Y('Topics:N')).properties(title="What topics are AI researchers focusing on?")
    st.altair_chart(acChart, use_container_width=True)

