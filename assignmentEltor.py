from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


consumer_key = 'consumerkey'
consumer_secret = 'secret'
access_token = '264955050-token'
access_token_secret = 'tokensecret'
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['Trump'])

import json
import pandas as pd
import matplotlib.pyplot as plt

tweets_data_path = '../data/twitter_data.txt'

tweets_data=[]
tweets_file = open(tweets_data_path, 'r')

for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue



