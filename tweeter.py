import tweepy
import random

import stocks


#read API keys and tokens from "keys" file
#use rstrip to remove newline from strings
f = open("keys.txt", "r")
consumer_key = f.readline()
consumer_key = consumer_key.rstrip('\n')
consumer_secret = f.readline()
consumer_secret = consumer_secret.rstrip('\n')
token = f.readline()
token = token.rstrip('\n')
token_secret = f.readline()
token_secret = token_secret.rstrip('\n')
#use these keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token, token_secret)
api = tweepy.API(auth)
print(api.me().name)






count = 1
#print home feed
tweets = api.home_timeline()
for tweet in tweets:
    print(str(count) + ":\t" + tweet.text)
    count += 1

#send a tweet
api.update_status(status='Test')
