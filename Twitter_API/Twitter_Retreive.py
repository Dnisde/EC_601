#!/usr/bin/env python
# encoding: utf-8
#Author - ZHAOZHONG QI

import requests
import tweepy # https://github.com/tweepy/tweepy
import json
#Twitter API credentials
consumer_key = "8KMps10UjAdfCZoLzUMOjJtaX"
consumer_secret = "wstgm1dNVCgnPWKiBJ1Z7EPnIjQGzrYgLwvUwvC6N2tQ7z1zFv"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAL5iUAEAAAAAmo6FYRjqdKlI3cNziIm%2BHUQB9Xs%3DS31pj0mxARMTOk2g9dvQ1yP9wknvY4FPBPUlE00smJcncw4dPR"

class twitter_access:

    def __init__(self,comsumer_Key, consumer_Secret):
        self.consumer_key = comsumer_Key
        self.consumer_secret = consumer_Secret
        # self.bearer_token = bearer_token


    def build_connections(self):

        auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
        try:
            api = tweepy.API(auth)
            for tweet in tweepy.Cursor(api.search_tweets, q='tweepy').items(10):
                print(tweet.text)

        except tweepy.TweepError:
            print('Error! Failed to get request token.')



    # def get_tweets(self):
    #     print("Get the tweets form server")

        # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        #
        # auth.set_access_token(access_tfoken, access_token_secret)
        #
        # api = tweepy.API(auth)
        #
        # public_tweets = api.home_timeline()
        # for tweet in public_tweets:
        #     print(tweet.text)


    # def get_all_tweets(screen_name):
    #
    #     #Twitter only allows access to a users most recent 3240 tweets with this method
    #
    #     #authorize twitter, initialize tweepy
    #     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    #     auth.set_access_token(access_key, access_secret)
    #
    #     api = tweepy.API(auth)
    #
    #     #initialize a list to hold all the tweepy Tweets
    #     alltweets = []
    #
    #     #make initial request for most recent tweets (200 is the maximum allowed count)
    #     new_tweets = api.user_timeline(screen_name = screen_name,count=10)
    #
    #     #save most recent tweets
    #     alltweets.extend(new_tweets)
    #
    #     #save the id of the oldest tweet less one
    #     oldest = alltweets[-1].id - 1
    #
    #     #keep grabbing tweets until there are no tweets left to grab
    #     while len(new_tweets) > 0:
    #
    #         #all subsiquent requests use the max_id param to prevent duplicates
    #         new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
    #
    #         #save most recent tweets
    #         alltweets.extend(new_tweets)
    #
    #         #update the id of the oldest tweet less one
    #         oldest = alltweets[-1].id - 1
    #         if(len(alltweets) > 15):
    #             break
    #         print("...%s tweets downloaded so far" % (len(alltweets)))
    #
    #     #write tweet objects to JSON
    #     file = open('tweet.json', 'w')
    #     print("Writing tweet objects to JSON please wait...")
    #     for status in alltweets:
    #         json.dump(status._json,file,sort_keys = True,indent = 4)
    #
    #     #close the file
    #     print("Done")
    #     file.close()

if __name__ == '__main__':

    web_app = twitter_access(consumer_key, consumer_secret)
    web_app.build_connections()
    # pass in the username of the account you want to download
    # get_all_tweets("@Ibra_official")
