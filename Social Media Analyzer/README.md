# Module of Social Media Analyzer

This is Introduction of our Social Media Analyzing program, which is mainly going to use the Twitter API and the Google NLP Engine to build a functionality analyzing tool to analyze the twitter's feeds. Basically, it is a briefly overview of the sentiment analysis tool by retrieve information from tweets that people post everyday. Or the feed of the publication and tweets from users, Then implementing the analysis and build different user cases for specific users.

## MileStone:

**Milestone & Sprint**
1. Realize both the Twitter API, and Google NLP(etc. might have more) to summary the usage and write the demo of test programs to exercise using different aspects of twitter API 2.0.  For instance, retrieving tweets, searching per time, hashtags, etc. Then Realize the Google NLP in AutoML Natrual Language part in specifically by the same way. Building a model and test the model's accurancy. Access and test the model by set up a script by using keywords on our own desktop.
2. Define and create the user Stories of our analyzing module / application, and showing how are we going to use them to building the innovation tool. This analyzer is basically of a combination of access Twitter API and Google NLP to learning to build a extension software based on MVP principle
3. Using MVP model to translate the user stories to the real modular design of the Social Media Analyzing tool. The user story might be predifined at the very beginning. But it might be altered by the changing in progress, or likewise, insteaded by better ideas to reconstruct the user stories in order to adapt with the Costumer demands under perspective of the blueprint gones well.
4. Finalize the Essential Story, use the essential story to reconstruct the Social Media Analyzer, Debug, Finish the program and close the project.


# 📝 About the Tool / Application itself.

[block:api-header]
{
  "title": "Social Media Analyzer"
}
[/block]
**Social Media Analyzer is principle of using Twitter API to retreive the sentiments data of features, such as a bulk of tweets, emotion icon and hashtags from the tweets in target. Then utilize those features into training the sentiment and predict those lables in different level perspectives by access the NLP model of Google Natrual Language tools.**

It is an analystic tool which help us to understand the API in depth, and realize the concept how we going to use the MVP and protocols to build our own product in the future practices. Writing Test Programs for third parties API, or implementing user stories by using the third parties API will be contained with this topic.


# 🚦 Interactive API Docs

### Twitter API [Reference](https://developer.twitter.com/en/docs/twitter-api/getting-started/important-resources)

* The Twitter API can be used to programmatically retrieve and analyze data, as well as engage with the conversation on Twitter **[Twitter API](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api)**. The Twitter API currently consists of two supported versions, as well as different access tiers. The listed information below is in order to help you better understand which version and tiers are available, but would recommend using the newest versions (Twitter API v2) where available. Learn more about our new [versioning strategy](https://developer.twitter.com/en/docs/twitter-api/versioning).
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


### Google Natrual Language Processing(NLP)/ AutoML: [Reference](https://cloud.google.com/natural-language/automl/docs/quickstart)

* AutoML Natural Language uses machine learning to analyze the structure and meaning of documents. You train a custom machine learning model to classify documents, extract information, or understand the sentiment of authors.
    * A classification model analyzes a document and returns a list of content categories that apply to the text found in the document.
    * An entity extraction model inspects a document for known entities referenced in the document and labels those entities in the text.
    * A sentiment analysis model inspects a document and identifies the prevailing emotional opinion within it, especially to determine a writer's attitude as positive, negative, or neutral.

The Google Natrual Language client Libraries access example of guideline shown at the following:

**Code Example: (In Python)**

```python
# Imports the Google Cloud client library
from google.cloud import language_v1

# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
text = u"Dear my love" # Test your own words of sentiment here!
document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

print("Text: {}".format(text))
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))
```


# 📈 User Story:

### Demo User Story:
> User Story 1
> As a journalist, I want to use the Social Media Analyzer to realize what kinds of twitter do people like to post during their daily life, and build the flash-news by those topics who owning high sentiments.

> User Story 2
> As a psychological counselor, I want to use the Social Media Analyzer to realize the patient's tempor in order to support him/her of customized service and compatible psychotherapy.

> User Story 3
> As a Data Scientist, I want to use the analyzer to build a specific dataset to help me look up the most-clicking rate tweets, and figure out the secrets behind those information.

> User Story 4
> As a commercial tenant, I want to retrieve the specific keywords,  and using the sentiment tool to help me analyze the point of view that if they like the merchandise or it needs room for improvement.

> User Story 5
> As an advertiser, I want to use the analyzer to utilize the sentiment of people's preference of those advertisement, and push those who they think more comfort to watch.


# 💬 Modular Design based on Selected Main Story

### Main User Story:

> 👍 User Story 1
>
> As a Data Scientist, I want to use the analyzer to build a User Survey based on looking up the most-clicking rate tweets of the keywords, and figure out who are they and sentiment information behind their tweets.

> 📘 User Story 2
>
> As a commercial tenant, I want to retrieve the specific keywords,  and using the sentiment tool to help me analyze the point of view that if they like the merchandise or it needs room for improvement.

### Modular Design:

**Code explaination: (in Python)**

```python

#!/usr/bin/env python
# encoding: utf-8
#Author - ZHAOZHONG QI

import requests
from flask import Flask, session
import json
import tweepy
import pandas as pd
import math
import argparse

# Imports the Google Cloud client library
from google.cloud import language_v1
client = language_v1.LanguageServiceClient.from_service_account_json(json_path)

#Twitter API credentials
consumer_key = "Your_Customer_Key"
consumer_secret = "Your_Customer_Secret"
json_path = "The_path_of_your_GoogleCloud_Client_Key"


class Social_Media_Analyzer:

    def __init__(self, comsumer_Key, consumer_Secret, keywords):
        self.consumer_key = comsumer_Key
        self.consumer_secret = consumer_Secret
        # self.bearer_token = bearer_token
        self.keywords = keywords
        self.twitters = []
        self.auth = ""

    def __repr__(self):
         return f"Social Media Analyzer analysis search based on keywords: {self.keywords} \n"

    def __call__(self):
        try:
            self.auth = tweepy.AppAuthHandler(self.consumer_key, self.consumer_secret)
            api = tweepy.API(self.auth, wait_on_rate_limit=True)
            tweets = tweepy.Cursor(api.search_tweets, q=self.keywords).items(1)
            userInfo = [tweet.user.screen_name for tweet in tweets]
            if not userInfo == None:
                print("Test connection Successful..\n")

        except:
            print("Bad request")

    def search_Bykeywords(self):

        search_words = self.keywords
        api = tweepy.API(self.auth, wait_on_rate_limit=True)
        new_search = search_words + " -filter:retweets"
       
        # Search the tweets hit by the keywords of number of #5
        tweets = tweepy.Cursor(api.search_tweets, q=search_words, lang="en", since="2020-01-01").items(10)
        for tweet in tweets:
            print(f"Twitter : {tweet.text}")
            self.twitters.append(tweet.text)

        self.evaluate_sentiment(self.twitters)
        return "Sentiment Analyze Finished based on keywords "



    def search_People_ByKeywords(self):
        search_words = self.keywords + " -filter:retweets"

        try:
            api = tweepy.API(self.auth, wait_on_rate_limit=True)
            tweets = tweepy.Cursor(api.search_tweets, q=search_words).items(10)
            userinfo = [tweet.user.screen_name for tweet in tweets]
            user_information = pd.DataFrame()
            for users in userinfo:
                users_tweets = api.user_timeline(screen_name=users)
                # users_tweets = tweepy.Cursor(api).items(3)
                tweet_list = []
                self.twitters = []
                for index, tweet in enumerate(users_tweets):
                    tweet_id = tweet.id # unique integer identifier for tweet
                    favorite_count = tweet.favorite_count
                    retweet_count = tweet.retweet_count
                    self.twitters.append(tweet.text)
                    created_at = tweet.created_at # utc time tweet created
                    source = tweet.source # utility used to post tweet
                    reply_to_user = tweet.in_reply_to_screen_name # if reply original tweetes screenname
                    retweets = tweet.retweet_count # number of times this tweet retweeted
                    favorites = tweet.favorite_count # number of time this tweet liked
                    # append attributes to list
                    tweet_list.append({'author': str(users),
                                       'favorite_count':favorite_count,
                                       'created_at':created_at,
                                       'favorites':favorites})
                # create dataframe
                df = pd.DataFrame(tweet_list, columns=['author',
                                                       'favorite_count',
                                                       'created_at',
                                                       'favorites'])

                # The first top twitter of each user's summery
                user_information = user_information.append(df.iloc[0, :], ignore_index=True)
                self.evaluate_sentiment(self.twitters, users)

            print(f"\nOverall information about all the users relevant about the keywords {self.keywords}: \n ")
            print(user_information)
            return user_information

        except:
            print("bad request")
            # print(e.message[0]['code'])  # prints 34
            # print(e.args[0][0]['code'])  # prints 34
        
    def evaluate_sentiment(self, twitters, userinfo=None):
        overall_score = 0
        # The text to analyze
        sentiment_sentences = twitters
        for index, sentence in enumerate(sentiment_sentences):
            document = language_v1.Document(content=sentence, type_=language_v1.Document.Type.PLAIN_TEXT)
            # Detects the sentiment of the text
            sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
            overall_score = overall_score + (sentiment.magnitude * sentiment.score)
            if userinfo is None:
                print("Twitter {} has a sentiment score of {}, strength of emotion: {}".format(index,  sentiment.score, sentiment.magnitude))
        

        if overall_score != 0:
            overall_score = overall_score / len(sentiment_sentences)
            if userinfo is not None:
                print(f"\nThe sensibility of User: '{userinfo}' is : {overall_score} \n "
                      f"(Higher indicates User is more Emotional, otherwise is Rational)\n")
            else:
                print(f"\nThe overall sentiment level based on the keywords '{self.keywords}': {overall_score} \n "
                      f"(Higher indicates positive mood, Lower indicates Negative mood)\n")


if __name__ == "__main__":
    # Utilize the analysis engine to search
    # Parameter 1: Your comsumer_key,
    # Parameter 2: Your comsumer_credentials / secret
    # Parameter 3: Key words that you want to search by the engine, either "brand" or "Buzz word"
    web_app = Social_Media_Analyzer(consumer_key, consumer_secret, "Disney Movies ratings")
    print(web_app)
    web_app()
    # Test Case 1 : Module Design for User Story 1: Data Scientist
    # web_app.search_People_ByKeywords()

    # Test Case 2: Module Design for User Story 2: commercial tenant
    # web_app.search_Bykeywords()
    
```

* **Test Case: Module Design for User Story 2 - Commercial tenant:**

* From the graph, `a commercial tenant (Disney Animation Pictures at here for example)` trying to use the keyword to access the ratings of his product,
At there, we search the tweets accessed by the keyword "Disney Movies Ratings", and we selected 10 instances by also adding with an extra filter with "retweets".

* ![Social_Media_0](https://user-images.githubusercontent.com/27568828/139638466-282f18c4-7cc6-49e9-b8b6-bbbbc86b5926.PNG)

* Example: As you could observed based on the graph, Top 10 of the list of tweets shows their sentiment score and magnitude of the content respectively. It is not hard to find
out the consistency of different people are verge to negative. Especially the tweet who retweeted the post on "post-pendemic era" since date after 2020-01-01. It looks like
the attitude of majority of how people like the movie which was less than satisfactory in the era of post-penmdemic.

* **Test Case: Module Design for User Story 1 - Data Scientist:**

* From the graph, it shows a basic example of how do a `Data Scientist using the keyword to retrieve the User information.`
* ![Social_Media_1 0](https://user-images.githubusercontent.com/27568828/139638925-bb9accf5-f24e-44f6-8eb2-456d6fe1a3ac.PNG)

* Example: The analyzer only does a simple screen out functionality, filter the users who retweet or comment most frequently based on the keyword triggered.
* The formula of the Sentiment point of each user which based on the properties of: Sentiment Score & Sentiment Magnitude from Engine of Google NLP analyzed.
* it is equals = the average sentiment points of top #(Maximum 20) tweets on the filterd user \n
               = Sum (Sentiment Score of each tweets * Sentiement Magnitude of each tweets) / # amount of tweets
           

* As you could observed, the highest socre of tweets of the user who most cares about around the `keyword` topic (We selected keyword = "happy" at here) reach up to 0.61, his/her character prefer more prefer optimistic (1 at highest)

* ![Social_Media_1](https://user-images.githubusercontent.com/27568828/139638492-ee05a92c-0402-4772-80d9-e0492c969adb.PNG)

* The lowest socre of tweets of the user who most cares about `keyword` topic which is only around 0.073, his/her character prefer more passive or calm (0 at lowest)

* ![Social_Media_2](https://user-images.githubusercontent.com/27568828/139638956-53cd17ea-eee1-4347-8487-d88639ffd2d2.PNG)


* And overall information of those user's tweets at the top of their homepage, which summerize at the following graph shown.\n
 `Favorite_count - favorite count`, `created_time - created at`, and `likes - favorite` basiclly has been selected as three information labels of about the people.
* ![Social_Media_3](https://user-images.githubusercontent.com/27568828/139639079-c8cbce26-a506-49ea-a88c-3f7682000558.PNG)


* It is a bascially example that shows how to utilize the social media analyzer to analyze what kind of character for the people who caring about the specific keywords in twitter's user group.
