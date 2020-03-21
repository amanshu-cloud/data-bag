import pandas as pd
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
import random
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



sa = SentimentIntensityAnalyzer()
sentiment_score = []
word_bag = []
data = pd.read_csv(r'C:\Users\Dell\Desktop\sqlpy\sqltutorial1\covid.csv')
words  = data['Abstract'].head(1)

positive = 0
negative = 0
compound = 0
neutral = 0
count = 0
for w in words:
    try:
        count+=1

        print(w+"\n")
        score = sa.polarity_scores(w)
        sentiment_score.append(score)
        positive+=score['pos']
        negative+=score['neg']
        compound+=score['compound']
        neutral+=score['neu']
    except TypeError :
        score = None
        sentiment_score.append(score)



print(sentiment_score)
print(f"averages \n positives = {positive/count}\nnegatives = {negative/count}\ncompound = {compound/count}\nneutral = {neutral/count}")