# word_cloud.py
# Word cloud generation.

import pandas as pd
import altair as alt
from textblob import TextBlob
import matplotlib.pyplot as plt
import streamlit as st
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def buildWordCloudText(data):
    text = ""
    for i in range(len(data)):
        text += data.text[i]
    return text


def getData(filename):
    data = pd.read_json(filename)
    return data


def getWordCloud(text):
    wordcloud = WordCloud(
        stopwords=STOPWORDS,
        max_font_size=50,
        max_words=150,
        background_color="white",
        collocations=False,
    ).generate(text)
    fig = plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    return fig


def getSentiment(data):
    sentiment = []
    for i in range(len(data)):
        avgSentiment = []
        blob = TextBlob(data.text[i])
        for sentence in blob.sentences:
            avgSentiment.append(sentence.sentiment.polarity)
        sentiment.append(avgSentiment)
    return sentiment


def getAvgSentiment(sentiments, data):
    docSentiments = []
    articleTitles = []
    for i in range(len(sentiments)):
        sentiment = 0
        for j in range(len(sentiments[i])):
            sentiment += sentiments[i][j]
        docSentiments.append((sentiment / len(sentiments[i])) * 100)
        articleTitles.append(data.title[i])
        tuples = list(zip(articleTitles, docSentiments))
        output = pd.DataFrame(tuples, columns=["Title", "Sentiment"])
    return output


def buildChart(data):
    sentChart = (
        alt.Chart(data)
        .mark_bar()
        .encode(
            alt.X(
                "Sentiment:Q",
                title="Media Sentiment of Articles about AI",
                scale=alt.Scale(domain=(-100, 100)),
            ),
            y="Title:O",
            color=alt.condition(
                alt.datum.Sentiment > 0, alt.value("steelblue"), alt.value("orange")
            ),
        )
        .properties(width=600)
    )
    return sentChart
