import tweepy
import random
import stocks
import datetime
#Go to Twitter developer account to find keys and copy paste them in order into keys.txt in same directory as this file

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
#Test if authentication worked by printed your username
print(api.me().name)




#print home feed
# count = 1
# tweets = api.home_timeline()
# for tweet in tweets:
#     print(str(count) + ":\t" + tweet.text)
#     count += 1

#send a tweet
ticker = "PCG"
if stocks.stock_info(ticker)[2] > 0:
    change = "up"
elif stocks.stock_info(ticker)[2] < 0:
    change = "down"
else:
    change = "unchanged"
message = ticker + " stock price is " + change + " $" + str(round(abs(stocks.stock_info(ticker)[2]), 2)) + " today from $" + str(round(stocks.stock_info(ticker)[0], 2)) + " to $" + str(round(stocks.stock_info(ticker)[1], 2)) + "\n\n" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "\nAutomatic update from https://github.com/evilpegasus/twitterbot"
print(message)
print(len(message))
api.update_status(status=message)
