#Importing necessary libraries
from pymongo import MongoClient
import re
import itertools
import collections
from matplotlib import pyplot

#Establishing connection to mongodb server
client = MongoClient('localhost:27017')

#Assigning a database and collection
tweet_collection = client.twitter.twicollection2

#Filtering Tweet field and its values from the collection
tweet_texts_list = [tweet['Tweet'] for tweet in tweet_collection.find()]

#Function to clean tweets from usernames, hyperlinks, special characters and converting it to lowercase
def clean_tweet(tweet_text):
	tweet_text = re.sub("@\S*\s?",'',tweet_text)
	tweet_text = re.sub("\n",' ',tweet_text)
	tweet_text = re.sub('([^0-9A-Za-z \t])|(\w+:\/\/\S+)','',tweet_text)
	tweet_text = tweet_text.lower()
	tweet_text = tweet_text.rstrip()
	return tweet_text

cleaned_tweet = [clean_tweet(tweet) for tweet in tweet_texts_list]

#Seperating the words in a tweet
split_tweet = [tweet_words.split() for tweet_words in cleaned_tweet]

#COmbining all the word into one list
combine_tweets = list(itertools.chain(*split_tweet))

#Synonyms of symptoms and their counters
fever = ['fever', 'feverishness', 'temperature', 'shivering', 'shiver']
fever_count = 0
cough = ['cough', 'cold', 'flu', 'hem', 'headache']
cough_count = 0
short_of_breath = ['asthmatic', 'choking', 'choke', 'breathing', 'breath', 'breathe', 'asthma']
sob_count = 0

#Iterating to update counters
for word in combine_tweets:
	if word in fever:
		fever_count += 1
	if word in cough:
		cough_count += 1
	if word in short_of_breath:
		sob_count += 1

#Creating a dictionary with their respective counters
word_dictionary={}
word_dictionary["Fever"] = fever_count
word_dictionary["Cough"] = cough_count
word_dictionary["Short_of_breath"] = sob_count
word_list = sorted(word_dictionary.items())

#Plotting a line graph for the above symptoms
x,y = zip(*word_list)
pyplot.plot(x,y, color="red")
pyplot.show()


