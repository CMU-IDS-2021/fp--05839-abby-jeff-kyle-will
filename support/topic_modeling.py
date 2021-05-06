# topic_modeling.py
# Topic model analysis for professional articles on machine intelligence.

import numpy as np
import pandas as pd
import altair as alt
import streamlit as st


def buildAcademicData(data):
    df = pd.DataFrame()
    topics = [
        "Language Models",
        "Cloud-Based ML Frameworks",
        "AI Based Multi-Lingual Translation",
        "Autonomous AI Decision Making",
        "Multi-Agent Pathfinding",
    ]
    years = []
    topic1, topic2, topic3, topic4, topic5 = [], [], [], [], []
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
    df["Topics"] = topics
    return df


def academic():
    years = {
        "2013": "2013",
        "2014": "2014",
        "2015": "2015",
        "2016": "2016",
        "2017": "2017",
        "2018": "2018",
        "2019": "2019",
        "2020": "2020",
        "2021": "2021",
    }
    data = pd.read_json("data/academicTopics.txt")
    acData = buildAcademicData(data)

    year = st.select_slider(
        "Select the year to see the popular topics in AI research.", list(years.keys())
    )
    nData = acData[int(year)]
    source = pd.DataFrame({"Number of Topics": nData.T, "Topics": acData["Topics"]})
    acChart = (
        alt.Chart(source)
        .mark_bar()
        .encode(
            x=alt.X("Number of Topics:Q", scale=alt.Scale(domain=(0, 20))),
            y=alt.Y("Topics:N"),
            color=alt.Color("Topics:N", scale=alt.Scale(scheme="redyellowblue")),
        )
        .properties(title="What topics are AI researchers focusing on?")
    )
    st.altair_chart(acChart, use_container_width=True)


def flipProfData(data):
    topics = [
        "Language Models",
        "Cloud-Based ML Frameworks",
        "AI Based Multi-Lingual Translation",
        "Autonomous AI Decision Making",
        "Multi-Agent Pathfinding",
    ]
    newData = data.drop("Topics", axis=1)
    newData = newData.T
    newData.columns = topics
    return newData


def topicTimeline(topic):
    unfixedData = pd.read_json("data/academicTopics.txt")
    data = buildAcademicData(unfixedData)
    data = flipProfData(data)
    nData = data[topic]
    years = ["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
    source = pd.DataFrame({"Years": years, "Number of Articles": nData.T})
    line = (
        alt.Chart(source)
        .mark_line(color="fcac64")
        .encode(x="Years", y="Number of Articles:Q")
        .properties(title="What topics are AI researchers focusing on?")
    )

    st.write(f"Lets look at {topic} research over time.")
    st.altair_chart(line, use_container_width=True)
