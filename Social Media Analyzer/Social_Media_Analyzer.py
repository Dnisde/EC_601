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
