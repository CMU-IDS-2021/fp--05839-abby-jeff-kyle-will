import pandas as pd
import numpy as np
import PIL
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

def buildWordCloudText(data):
    text = ''
    for i in range(len(data)):
        text += data.text[i]
    return text

def getData(filename):
    data = pd.read_json(filename)
    return data

def displayWordCloud(text):
    wordcloud = WordCloud(stopwords=STOPWORDS, max_font_size=50, max_words=150, 
                   background_color="white", collocations=False).generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def getSentiment(data):
    sentiment = []
    for i in range(len(data)):
        avgSentiment = []
        blob = TextBlob(data.text[i])
        for sentence in blob.sentences:
            avgSentiment.append(sentence.sentiment.polarity)
        sentiment.append(avgSentiment)
    return sentiment
        
def getAvgSentiment(sentiments):
    docSentiments = []
    for i in range(len(sentiments)):
        sentiment = 0
        for j in range(len(sentiments[i])):
            sentiment += sentiments[i][j]
        docSentiments.append(sentiment/len(sentiments[i]))
    return docSentiments
    

df = getData("../articles.json")
txt = buildWordCloudText(df)
displayWordCloud(txt)
sent = getSentiment(df)
finalSent = getAvgSentiment(sent)
print(finalSent)
