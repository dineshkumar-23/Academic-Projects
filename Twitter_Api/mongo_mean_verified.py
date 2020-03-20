#Importing the necessary libraries
from pymongo import MongoClient
import re
import pprint
import itertools
import collections
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import plotly.express as px
import pprint

#Establishing connection with the mongodb server
client = MongoClient('localhost:27017')

#Creating a database and a collection in mongodb
tweet_collection = client.twitter.twicollection2

#Filtering the 'Tweet' field and its value from the collection
tweet_texts_list = [tweet['Tweet'] for tweet in tweet_collection.find({"Verified":True})]
pprint.pprint(tweet_texts_list)


#Defining a function to remove special characters and URL's
def clean_tweet(tweet_text):
    tweet_text = re.sub("\n",' ',tweet_text)
    tweet_text = re.sub('([^0-9A-Za-z \t])|(\w+:\/\/\S+)','',tweet_text)
    return tweet_text

#Passing the parameter 'tweet' in the function clean_tweet
cleaned_tweet = [clean_tweet(tweet) for tweet in tweet_texts_list]

#Seperating the words in each tweet and calculating length of each tweet
tweet_length = [len(tweet_words.split()) for tweet_words in cleaned_tweet]
#print(tweet_length)

#Calculating the mean value of length of tweets
average_tweet_length = np.mean(tweet_length)

print(average_tweet_length)

#Calculating the Interquartile range for the length of tweets
quartile_1, quartile_3= np.percentile(tweet_length,[25,75])
print(quartile_1)
print(quartile_3)

#Plotting a normal distribution graph for length of tweets
tweet_length.sort()
tl_mean = np.mean(tweet_length)
tl_std = np.std(tweet_length)
pdf = stats.norm.pdf(tweet_length, tl_mean, tl_std)
plt.plot(tweet_length, pdf)
plt.show()

df = pd.DataFrame(dict(
    linear=tweet_length)).melt(var_name="quartilemethod")


fig = px.box(df, y="value", facet_col="quartilemethod", color="quartilemethod",
             boxmode="overlay", points='all')

fig.update_traces(quartilemethod="linear", jitter=0, col=1)

fig.show()

