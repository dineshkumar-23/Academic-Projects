#Importing the necessary libraries
from kafka import KafkaConsumer
from pymongo import MongoClient
import json

#Establishing a connection with mongodb server
client = MongoClient('localhost:27017')

#Creating a database and collection in mongodb
collection = client.twitter.twittercollection

#Pulling the messages from producer
consumer = KafkaConsumer(
    'twitterdata',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='groupsss38',
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))

#Filtering the required fields from the raw twitter data
for line in consumer:
    json_load = json.dumps(line.value)
    json_data = json.loads(json_load)
    if(json_data['lang']== "en"):
        send_data = '{}'
        jsonsenddata = json.loads(send_data)
        if "retweeted_status" in json_data:
            try:
                jsonsenddata = json_data['retweeted_status']['extended_tweet']['full_text']
            except:
                jsonsenddata = json_data['retweeted_status']['text']
        else:
            try:
                jsonsenddata = json_data['extended_tweet']['full_text']
            except:
                jsonsenddata = json_data['text']
        data_country = '{}'
        json_send_country = json.loads(data_country)
        if "place" in json_data:
            try:
                json_send_country = json_data['place']['country']
            except:
                json_send_country = json_data['place']
        else:
            pass

    #
    dictionary=dict()
    dictionary['Time'] = json_data["created_at"]
    dictionary['Screenname'] = json_data["user"]["screen_name"]
    dictionary['Username'] = json_data["user"]["name"]
    dictionary['Location'] = json_data["user"]["location"]
    dictionary['Favourites_count'] = json_data["favorite_count"]
    dictionary['Retweet_count'] = json_data["retweet_count"]
    dictionary['Reply_count'] = json_data["reply_count"]
    dictionary['Tweet'] = jsonsenddata
    dictionary['Tweeted_Location'] = json_send_country
    dictionary['Users_Followers_Count'] = json_data["user"]["followers_count"]
    dictionary['Verified_User'] = json_data["user"]["verified"]
    dictionary['Users_Fav_Tweet'] = json_data["user"]["favourites_count"]
    print(dictionary)
    collection.insert_one(dictionary)
