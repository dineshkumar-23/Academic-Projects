from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pykafka import KafkaClient

API_KEY = 'obtained from developer account'
API_SECRET_KEY = 'obtained from developer account'
ACCESS_TOKEN = 'obtained from developer account'
ACCESS_TOKEN_SECRET= 'obtained from developer account'

client = KafkaClient(hosts="localhost:9092")
topic = client.topics['Twitter']
producer = topic.get_sync_producer()


class StdOutListener(StreamListener):
    def __init__(self, fetched_tweets_filename):
        super().__init__()
        self.fetched_tweets_filename = fetched_tweets_filename
        self.counter = 0
        self.limit = 2000000

    def on_data(self, data):
        try:
            if self.counter < self.limit:
                self.counter += 1
                print(data)
                with open(self.fetched_tweets_filename, 'a') as tf:
                    tf.write(data)
                producer.produce(data.encode('ascii'))
                return True
            else:
                return False
        except BaseException as e:
            pass

#To check if twitter has issued notice on rate limit, if yes then break the stream

    def on_error(self, status):
        if status == 420:
        	return false
        print(status)


if __name__ == "__main__":
    fetched_tweets_filename = "tweets_limits_2.txt"
    auth = OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    listener = StdOutListener(fetched_tweets_filename)
    stream = Stream(auth, listener)
    stream.filter(track=['#SuperBowl'])


