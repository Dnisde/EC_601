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
**Code Example:**
[block:code]
{
  "codes": [
    {
      "code": "import requests\nimport tweepy # https://github.com/tweepy/tweepy\nimport json\n\n#Twitter API credentials\nconsumer_key = <your_comsumer_key_API_Developer>\nconsumer_secret = <your_comsumer_secret_API_Developer>\nbearer_token = <your_bearer_token_API_Developer>\n\ndef build_connections(self):\n  auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)\n  try:\n    api = tweepy.API(auth)\n    for tweet in tweepy.Cursor(api.search_tweets, q='tweepy').items(10):\n      print(tweet.text)\n      \n  except tweepy.TweepError:\n    print('Error! Failed to get request token.')\n\nbuild_connections()",
      "language": "python"
    }
  ]
}
[/block]
### Google Natrual Language Processing(NLP)/ AutoML: [Reference](https://cloud.google.com/natural-language/automl/docs/quickstart)

* AutoML Natural Language uses machine learning to analyze the structure and meaning of documents. You train a custom machine learning model to classify documents, extract information, or understand the sentiment of authors.
    * A classification model analyzes a document and returns a list of content categories that apply to the text found in the document.
    * An entity extraction model inspects a document for known entities referenced in the document and labels those entities in the text.
    * A sentiment analysis model inspects a document and identifies the prevailing emotional opinion within it, especially to determine a writer's attitude as positive, negative, or neutral.

The Google Natrual Language client Libraries access example of guideline shown at the following:

**Code Example:**
[block:code]
{
  "codes": [
    {
      "code": "# Imports the Google Cloud client library\nfrom google.cloud import language_v1\n\n# Instantiates a client\nclient = language_v1.LanguageServiceClient()\n\n# The text to analyze\ntext = u\"Dear my love\" # Test your own words of sentiment here! \ndocument = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)\n\n# Detects the sentiment of the text\nsentiment = client.analyze_sentiment(request={'document': document}).document_sentiment\n\nprint(\"Text: {}\".format(text))\nprint(\"Sentiment: {}, {}\".format(sentiment.score, sentiment.magnitude))",
      "language": "python"
    }
  ]
}
[/block]

# 📈 User Story

[block:callout]
{
  "type": "warning",
  "title": "User Story 1",
  "body": "As a journalist, I want to use the Social Media Analyzer to realize what kinds of twitter do people post during their daily life."
}
[/block]

[block:callout]
{
  "type": "success",
  "title": "User Story 2",
  "body": "As a psychological counselor, I want to use the Social Media Analyzer to realize the patient's tempor in order to support with custom and compatible psychotherapy."
}
[/block]

[block:callout]
{
  "type": "info",
  "title": "User Story 3"
}
[/block]

[block:callout]
{
  "type": "warning",
  "title": "User Story 4",
  "body": "As a doctor, I wanted to be alerted when the patient pulse go below or above a limit"
}
[/block]

[block:callout]
{
  "type": "success",
  "title": "User Story 5",
  "body": "As a doctor, I want to look at my patients vitals for any period of time."
}
[/block]
As a Twitter D
