# About Module of Social Media Analyzer ReadMe! :owlbert:

This is Introduction of our Social Media Analyzing program, which is mainly going to use the Twitter API and the Google NLP Engine to build a functionality analyzing tool to analyze the twitter's feeds. Bascially, it is start from the sentiment of text twitter feed of the publication and tweets from users.

## MileStone:

**Our milestone are basically divided into three essential part:**
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


# 📈 User Story

> 👍 User Story 1
>
> As a journalist, I want to use the Social Media Analyzer to realize what kinds of twitter do people like to post during their daily life, and build the flash-news by those topics who owning high sentiments.

> 📘 User Story 2
>
> As a psychological counselor, I want to use the Social Media Analyzer to realize the patient's tempor in order to support him/her of customized service and compatible psychotherapy.

> 👍 User Story 3
>
> As a Data Scientist, I want to use the analyzer to build a specific dataset to help me look up the most-clicking rate tweets, and figure out the sercret behind those information.

> 📘 User Story 4
>
> As a commertial tenant, I want to retreive the specific keywords,  and using the sentiment tool to help me analyze the point of view that if they like the merchandise or it needs room for improvement.

> 👍 User Story 5
>
> As a advertiser, I want to use the analyzer to utilize the sentiment of people's preference of those advertisement, and push those who they think more comfort to watch.


## 💬 Conclusion

### Coming Soon...
