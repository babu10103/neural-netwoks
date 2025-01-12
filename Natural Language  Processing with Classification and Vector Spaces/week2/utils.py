import re
import string
import nltk
from nltk.corpus import twitter_samples
import matplotlib.pyplot as plt
import random
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer


# step1: download the data
# nltk.download('twitter_samples')

# step 2: load the positive and negative tweets

# step 3: raw text processing for sentiment analysis
# 1. tokenizing
# 2. lowercasing
# 3. removing stop words and punctuations
# 4. stemming


# download stopwords from nltk
# nltk.download('stopwords')

# remove hyperlinks, twitter marks, styles

def process_tweet(tweet):

    # print('\033[92m' + tweet)
    # print('\033[94m')

    tweet2 = re.sub(r'^RT[\s]+', '', tweet)
    tweet2 = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet2)
    tweet2 = re.sub(r'#', '', tweet2)
    # print(tweet2)

    # print('\033[92m')
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    tweet_tokens = tokenizer.tokenize(tweet2)
    # print(tweet_tokens)
    # print('\033[0m')


    stopwords_english = set(stopwords.words('english'))
    # print('Stop words: \n')
    # print(stopwords_english)

    # print('Punctuations: \n')
    # print(string.punctuation)
    punctuations = set(string.punctuation)

    clean_tokens = []
    for token in tweet_tokens:
        if token not in stopwords_english and token not in punctuations:
            clean_tokens.append(token)

    # print("print stop words and punctuations: ")
    # print('clean tokens')

    # stemming
    stemmer = PorterStemmer()
    stemmed_tokens  = []
    for token in clean_tokens:
        stemmed_tokens.append(stemmer.stem(token))

    # print(stemmed_tokens)
    return stemmed_tokens

def build_freqs(tweets, ys):
    """
    Input:
        tweets: list of tweets
        ys: an m x 1 matrix with the sentiment label for each tweet (either 0 or 1)
    
    Output:
        freqs: a dict mapping each (word, sentiment) pair to its frequency
    """
    yslist = np.squeeze(ys).tolist()
    freqs = {}
    for y, tweet in zip(yslist, tweets):
        for word in process_tweet(tweet):
            pair = (word, y)
            if pair in freqs:
                freqs[pair] += 1
            else:
                freq[pair] = 1
    return freqs

# print(help(np.squeeze))
