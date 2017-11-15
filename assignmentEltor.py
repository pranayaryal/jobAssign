from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


consumer_key = 'Pw3hYPmzu41ksHZcDNJ4Vbbaw'
consumer_secret = 'sV0vaEtfkjwsDt2g65LbvTaB8ixcQk9ML0CG6KD19ClOWeHr53'
access_token = '264955050-qvXdW9Misz9FjHv5OETNOAv10WV5ApuVVuIGHqLc'
access_token_secret = 'ZitVR3GiYHzzBQKQZgi1lOdz8eZsWtBqGixX0aj7KCQRH'
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



