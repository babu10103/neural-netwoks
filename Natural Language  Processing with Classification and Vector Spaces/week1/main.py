from nltk.corpus import twitter_samples
from utils.utils import process_tweets


pos_tweets = twitter_samples.strings('positive_tweets.json')
neg_tweets = twitter_samples.strings('negative_tweets.json')

print(process_tweets(pos_tweets[2277]))

 