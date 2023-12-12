import tweepy
from twitter_keys import access_token, access_token_secret, consumer_key , consumer_secret , bearer_token
import emoji
from main import tweet as tw

client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token,access_token_secret)

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token,access_token_secret)
api = tweepy.API(auth)

client.create_tweet(text = emoji.emojize(tw))
print("tweeted!")