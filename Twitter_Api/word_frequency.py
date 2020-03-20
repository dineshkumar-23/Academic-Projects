import os
import tweepy as tw
import pandas as pd
import re
import collections
import itertools
import pprint
from collections import Counter
from matplotlib import pyplot as plt

#Assigning variables for each key
consumer_key= 'obtained from developer account'
consumer_secret= 'obtained from developer account'
access_token= 'obtained from developer account'
access_token_secret= 'obtained from developer account'

#Authentication process
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#Enter the search term that need to be analyzed in twitter
search_words = "coronavirus"
date_since = "2020-01-15"

#Using cursor method filter the required search term
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(10)
for tweet in tweets:
   pprint.pprint(tweet)

#Get the tweets in the form of list using list comprehension method
tweet_list = [tweet.text for tweet in tweets]
pprint.pprint(tweet_list)

#Replace URLs found in a text string with nothing
#(i.e. it will remove the URL from the string).
def remove_url(txt):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

tweet_list_no_url = [remove_url(tweet) for tweet in tweet_list]

#splitting the words in each tweet and lowercasing each word to make it similar
split_words = [tweet_words.lower().split() for tweet_words in tweet_list_no_url]
pprint.pprint(split_words)

#Flattening the list (i.e) putting all the words in each list into one list
flatten_list = list(itertools.chain(*split_words))
pprint.pprint(flatten_list)

#creating a Counter (C in counter must be uppercase)
word_count = collections.Counter(flatten_list)
print(word_count.most_common(15))

#creating a dataframe using pandas
tweet_word_frequency = pd.DataFrame(word_count.most_common(15),
                             columns=['words', 'count'])

word_frequency_csv = tweet_word_frequency.to_csv(r'C:/Users/Dinesh/Desktop/word_freq.csv', index = None, header = True)
print(tweet_word_frequency)

#plotting a horizontal bar graph based on the dataframe
fig, ax = plt.subplots(figsize=(8, 8))

tweet_word_frequency.sort_values(by='count').plot.barh(x='words',
                      y='count',
                      ax=ax,
                      color="purple")

ax.set_title("Common Words Found in Tweets (Including All Words)")

plt.show()

















