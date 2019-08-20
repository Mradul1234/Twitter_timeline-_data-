import tweepy
from tweepy import OAuthHandler
ACCESS_TOKEN = "1099038746001850368-gjTnSyMSDSkTUXmRuBzbWQ74Wl21au"
ACCESS_TOKEN_SECRET = "2duV3bDBDOq6l5yOJ5koZerrKiUa0i6QpvH6sJWetaPzm"
CONSUMER_KEY = "voqGMN0PBFcuXZEF0Wh0zOdxZ"
CONSUMER_SECRET = "a2UCmZq4G8lgK1gSf1WoXWxB9wmvuxSHfFqcoxjh7nGCOMbZGO"

 
auth=OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api=tweepy.API(auth)
for status in tweepy.Cursor(api.home_timeline).items(10):
      #  Process a single status
    print(status.text)
 
public_tweets=api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

name="@dm_ghaziabad"
tweetCount= 20
results = api.user_timeline(id=name, count=tweetCount)
for tweet in results:
    print (tweet.text)

