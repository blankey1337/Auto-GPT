import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

def send_tweet(tweet_text):
    consumer_key = os.environ.get("TW_CONSUMER_KEY")
    consumer_secret= os.environ.get("TW_CONSUMER_SECRET")
    access_token= os.environ.get("TW_ACCESS_TOKEN")
    access_token_secret= os.environ.get("TW_ACCESS_TOKEN_SECRET")

    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    # Send tweet
    try:
        client.create_tweet(text=tweet_text)
        return "Tweet sent successfully!"
    except tweepy.TweepyException as e:
        return "Error sending tweet: {}".format(e)
