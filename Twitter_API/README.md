# About Module of Twitter API ReadMe:

This is Introduction of our retreive program, which is mainly going to use the Twitter API to build a functionality library that analyzes twitter feeds:  sentiment of text twitter feed.

### MileStone:

**Our milestone are basically divided into three essential part:**
1. Realize what is Twitter API, summary the usage and write the demo of test programs to exercise different twitter APIs.  For example, retrieving tweets, searching per time, hashtags, etc.
2. Define and create the user Stories of our module / application, and showing how are we going to use them to build something differently and innovation.
3. Using MVP model to translate the user stories to our real modular design

# 📝 About the Twitter API itself

The Twitter API can be used to programmatically retrieve and analyze data, as well as engage with the conversation on Twitter. **[Twitter API](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api)**
The Twitter API currently consists of two supported versions, as well as different access tiers. The listed information below is in order to help you better understand which version and tiers are available, but would recommend using the newest versions (Twitter API v2) where available. Learn more about our new [versioning strategy](https://developer.twitter.com/en/docs/twitter-api/versioning).


# 🚦 Interactive API Docs

### Twitter API [Reference](https://developer.twitter.com/en/docs/twitter-api/getting-started/important-resources)

* **API Keys Retreive Example:** Twitter API v2 [right in the docs](https://docs.readme.com/docs/custom-login-with-readme), so they can play around with your API right inside ReadMe.

The Twitter API 2.0 OAuth 2 Authentication Guideline Code shown at the following (tweepy - Library):

**Code Example: (in Python)**

```python
import requests
import tweepy # https://github.com/tweepy/tweepy
import json

#Twitter API credentials
consumer_key = <your_comsumer_key_API_Developer>
consumer_secret = <your_comsumer_secret_API_Developer>
bearer_token = <your_bearer_token_API_Developer>

def build_connections(self):
  auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
  try:
    api = tweepy.API(auth)
    for tweet in tweepy.Cursor(api.search_tweets, q='tweepy').items(10):
      print(tweet.text)

  except tweepy.TweepError:
    print('Error! Failed to get request token.')

build_connections()
```
The above is just using a very simple case to retreive the public information which access to read-only authority in Tweets and Retweets.


# 💬 Conclustion

**Retreiving and test the using of Twitter API is the best way to practice how to access the target information that we might want to utulize.**

* Twitter API has a lot of specific attributes, it will not only restriced by as similar as the way of using web crawler.
* Twitter has **tweets, Users, Direct Messages, Lists, Trends, Media and Places** that could be accessed in many different ways, in multiples of one time retreive . It depends on what kinds of information that might be useful for sentiment analysis.
